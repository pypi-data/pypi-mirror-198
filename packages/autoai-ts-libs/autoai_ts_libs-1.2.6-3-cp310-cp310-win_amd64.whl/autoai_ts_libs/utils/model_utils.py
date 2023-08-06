# ************* Begin Copyright - Do not add comments here **************
#   Licensed Materials - Property of IBM
#
#   (C) Copyright IBM Corp. 2021, 2022, All Rights Reserved
#
# The source code for this program is not published or other-
# wise divested of its trade secrets, irrespective of what has
# been deposited with the U.S. Copyright Office.
# **************************** End Copyright ***************************

import pandas as pd
import numpy as np
from autoai_ts_libs.watfore.watfore_utils import WatForeUtils
from autoai_ts_libs.utils.messages.messages import Messages

class Model_utils:
    @classmethod
    def get_names_from_autoai_estimator(cls, autoai_est):
        """
        Get pipeline name ane estimator name from estimator 
        :param est:
        :return: pipeline name and estimator name
        """
        if hasattr(autoai_est, "named_steps"):
            ae_est = autoai_est.named_steps["windowedttr"].regressor.named_steps["est"]
            if hasattr(ae_est, "regressor"):
                est_name = ae_est.regressor._name
            else:
                est_name = ae_est._name
            is_exogenous_pipeline = autoai_est.named_steps["windowedttr"].is_exogenous_pipeline_
        else:
            est_name = autoai_est.short_name
            is_exogenous_pipeline = autoai_est.is_exogenous_pipeline_

        if 'RandomForest' in est_name:
            est_name = 'RandomForest'
            if is_exogenous_pipeline:
                pipeline_name = "ExogenousRandomForestRegressor"
            else:
                pipeline_name = "RandomForestRegressor"
        elif ('SVR' in est_name) or ('SVM' in est_name):
            est_name = 'SVM'
            if is_exogenous_pipeline:
                pipeline_name = "ExogenousSVM"
            else:
                pipeline_name = "SVM"

        return pipeline_name, est_name
    
    @classmethod
    def get_names_from_srom_estimator(cls, srom_est):
        """
        Get individual pippline name specified by user according to each pipeline of SROM 
        Input:
            est: object, an estimator from ranked pipeline
        Output:
            pipeline name: string
        """
        pipeline_name=""

        est_name = srom_est.__class__.__name__
        # target_columns = srom_est.target_columns
        # feature_columns = srom_est.feature_columns
        
        # has_exo = bool(set(feature_columns) - set(target_columns))
        has_exo = srom_est.is_exogenous_pipeline_

        if has_exo:
            if 'LocalizedFlatten' in est_name:
                pipeline_name = 'ExogenousLocalizedFlattenEnsembler'
            elif 'DifferenceFlatten' in est_name:
                pipeline_name = 'ExogenousDifferenceFlattenEnsembler'
            elif 'Flatten' in est_name:
                pipeline_name = 'ExogenousFlattenEnsembler'
            elif 'MT2RForecaster' in est_name:
                pipeline_name = 'ExogenousMT2RForecaster'
        else:
            if 'LocalizedFlatten' in est_name:
                pipeline_name = 'LocalizedFlattenEnsembler'
            elif 'DifferenceFlatten' in est_name:
                pipeline_name = 'DifferenceFlattenEnsembler'
            elif 'Flatten' in est_name:
                pipeline_name = 'FlattenEnsembler'
            elif 'MT2RForecaster'in est_name:
                pipeline_name = 'MT2RForecaster'
        
        return pipeline_name
    
    @classmethod
    def get_names_from_watfore_estimator(cls, watfore_est):
        """
        Get individual pippline name specified by user according to each pipeline of Watfore 
        Input:
            est: object, an estimator from ranked pipeline
        Output:
            pipeline name: string
        """
        pipeline_name=""
        algo_name= watfore_est.algorithm
        algo_type = watfore_est.algorithm_type
        if algo_name == "hw" and algo_type == "additive":
            pipeline_name = "HoltWinterAdditive"
        elif algo_name == "hw" and algo_type == "multiplicative":
            pipeline_name = "HoltWinterMultiplicative"
        elif algo_name == "arima": 
            pipeline_name = "ARIMA"
        elif algo_name == "bats": 
            pipeline_name = "Bats"
        elif algo_name == "arimax_dmlr": 
            pipeline_name = "ARIMAX_DMLR"
        elif algo_name == "arimax": 
            pipeline_name = "ARIMAX"
        elif algo_name == "arimax_palr": 
            pipeline_name = "ARIMAX_PALR"
        elif algo_name == "arimax_rsar":
            pipeline_name = "ARIMAX_RSAR"
        elif algo_name == "arimax_rar": 
            pipeline_name = "ARIMAX_RAR"

        return pipeline_name
    
    @classmethod
    def get_ts_model_type(cls, pipeline_name):
        model_type = "non-exogenous"
        if "Exogenous" in pipeline_name or "ARIMAX" in pipeline_name:
            model_type = "exogenous"

        return model_type


def prepare_ground_truth(a, stepsize=1, prediction_horizon=1):
    """
    Input: a [N, D] as 2D ary
    Output:
        [nSmp, nDim] 2D ary, where
            nDim = [D*prediction_horizon] (row-wise stack)

    Each row in the outputted 2D array is created as:
        - A flatten 1D ary [D*prediction_horizon,]
        - skip stepsize in a to create next row for the output 2D ary

    Example:
        y2D = np.array([[1, 2],
                        [3, 4],
                        [5, 6],
                        [7, 8]])

        y = _prepare_ground_truth(y2D, prediction_horizon=4)
            [[1 2 3 4 5 6 7 8]]

        y = _prepare_ground_truth(y2D, prediction_horizon=3)
            [[1 2 3 4 5 6]
             [3 4 5 6 7 8]]

             y.flatten()
            [1 2 3 4 5 6 3 4 5 6 7 8]

        y = _prepare_ground_truth(y2D, prediction_horizon=2)
            [[1 2 3 4]
             [3 4 5 6]
             [5 6 7 8]]

             For metric evaluation on each component TS, y will be reshaped as follows:
                 [[1 2]
                 [3 4]
                 [3 4]
                 [5 6]
                 [5 6]
                 [7 8]] (6, 2)

        # role of stepsize > 1:
        y = _prepare_ground_truth(y2D, prediction_horizon=2, stepsize=2)
            [[1 2 3 4]
             [5 6 7 8]]

"""

    n = a.shape[0]
    return np.hstack(
        a[i: 1 + n + i - prediction_horizon: stepsize]
        for i in range(0, prediction_horizon)
    )

def compute_prediction_accuracy(y, y_pred, ph, ppy='average', verbose=False):
    """
    Compute prediction accuracy by comparing y_pred against groundtruth y.
    Entries with nan values in y will be ignored from computing accuracy.
    If ph < len(y), there are many predictive values in y_pred for each timepoint in y
    and thus their averaged value will be used as the final predictive value if ppy='average'.
    If sppy = 'original', y will be re-generated to match the size of y_pred prior to computing accuracy.

    Input:
        + y [nSmp,nDim]: ground truth time series (holdout set), with nSmp = holdout_size, nDim = nTS
        + y_pred [nSmp2,nDim]: predicted values from a pipeline, with nSmp2 = ph*(hn-ph+1), nDim = nTS
        + ph: prediction horizon
        + ppy: 'average' or 'original' to specify how predicted values at each timestamp is aggregated

    Output:
        + mae/mse/smape/r2: each is a list of 1 entry for UTS, nTS entries for MTS
        + y_pred_avg [nSmp,nDim]: avg of y_pred with the same shape of 2D array as of y

    Example 1, computing y_pred_avg from y_pred in UTS:
        - Last 6 timepoints (1,2,3,4,5,6) are used for the holdout set y
        - Prediction horizon ph=3
        - Then there will be 4 steps of prediction until the last predictive value of a pipeline
        reaches the last timepoint of y:  (1,2,3), (2,3,4), (3,4,5), (4,5,6)
        And the pipeline stacks them all as a single matrix: (1,2,3,2,3,4,3,4,5,4,5,6)
        - So, predictive values are averaged from these 4 tuples at 6 timestamps as follows:
            (1,(2,2),(3,3,3),(4,4,4),(5,5),6)
        - For instance:

            # Groundtruth holdout set y:
            y = np.asarray([[1.],[2.],[3.],[4.],[5.],[6.]]) #(6, 1)

            # Predictive array returned by a pipeline (shape of [nSmp2,1]):
            y_pred = np.asarray([1.1,2.1,3.1, 2.2,3.2,4.2, 3.3, 4.3, 5.3, 4.4, 5.4,6.4]).reshape(-1,1) # returned

            # which implies the actual y_pred at 4 timestamp is:
            #y_pred =[
                     [1.1 2.1 3.1]     # 1st prediction at 1st time stamp of holdout set
                     [2.2 3.2 4.2]     # 2nd prediction at 2nd time stamp of holdout set, etc.
                     [3.3 4.3 5.3]
                     [4.4 5.4 6.4]     # 6.4 reaches the last timestamp, i.e. corresponding to [6.] in y
                     ]

            y_pred_avg = avg_y_pred(y,y_pred,ph=3,hn=6)
            print('\n y_pred_avg: \n',y_pred_avg)

            # Then, y_pred_avg is:
                         [[1.1 ]
                         [2.15]
                         [3.2 ]
                         [4.3 ]
                         [5.35]
                         [6.4 ]]


        Example 2, computing y_pred_avg from y_pred for Bivariate time series (MTS):
            - Last 4 timestamps are used for the holdout set y
            - Prediction horizon ph=3
            - Then there will be only 2 steps of prediction until a pipeline reaches the last timestamp of y: (1,2,3), (2,3,4)
            - The pipeline stacks and returns values at timestamps: (1,2,3,2,3,4)
            - And this function averages out at timestamps: (1,(2,2),(3,3),4)
            - For instance:

                y = np.asarray([[1, 10], [2,20], [3,30], [4,40]])
                y_pred = np.asarray([
                                    [1.1, 10.1],
                                    [2.2, 20.2],
                                    [3.1, 30.1],
                                    [2.1, 20.1],
                                    [3.1, 30.1],
                                    [4.0, 40.0]
                                    ])
                (mae,mse,r2,smape, y_pred) = avg_y_pred(y,y_pred,ph=3)
                 # Then, y_pred_avg is:
                     [
                     [ 1.1  10.1 ]
                     [ 2.15 20.15]
                     [ 3.1  30.1 ]
                     [ 4.   40.  ]]     # (4, 2), comparable to y above



    """

    def __compute_on_one_series(y1D, y_pred1D, ph, verbose):
        """
        Goal: Average out 1 univariate time series
        Input:
            + y1D: 2D ary [nSmp1,1]
            + y_pred1D: 2D ary [nSmp2,1]
        Output:
            + y_pred1D_avg: 2D ary [nSmp1,1], same shape as y1D
            + mae1D, mse1D, r21D, smape1D: accuracy wrt 1 time series, each as a scalar
        """

        if verbose:
            print("\n== y1D.shape, y_pred1D.shape: ", y1D.shape, y_pred1D.shape)

        # reshape y_pred1D to [nTimeStamp, ph]
        y_pred1D = y_pred1D.reshape(-1, ph)

        """
        To compute average value at each timestamp:
            - Convert y_pred1D to a list, each entry has "ph" predictive values
            - Append nan entries at begin of each list's entry appropriately 
                in order to align timestamp.
            - Convert the list to df and take column average (excluding nan entries),
            each column of the df corresponds to one timestamp 
            - Convert that column average vector into [nSmp,1] array
        """
        y_pred_list = y_pred1D.tolist()

        yp = []
        for i in range(len(y_pred_list)):
            ynan = np.empty((i))
            ynan[:] = np.nan
            ynan = ynan.tolist()
            ynan.extend(y_pred_list[i])
            yp.append(ynan)
            if verbose:
                print(i, ynan)

        # convert to dataframe to compute column-wise average
        df = pd.DataFrame(data=yp, index=None)

        y_pred1D_avg = df.mean(axis=0, skipna=True)
        y_pred1D_avg = np.asarray(y_pred1D_avg).reshape(-1, 1)

        # accuracy
        (mae1D, mse1D, r21D, smape1D) = WatForeUtils.compute_metrics(
            y1D, y_pred1D_avg
        )
        return (mae1D, mse1D, r21D, smape1D, y_pred1D_avg)

    if (isinstance(y, list)):
        column_is_target = False
        number_targets = len(y)
    else:
        column_is_target = True
        number_targets = y.shape[1]

    if verbose:
        if (column_is_target):
            print("\n== y.shape, y_pred.shape: ", y.shape, y_pred.shape)
        else:
            print("\n== len(y), len(y_pred): ", len(y), len(y_pred))
        print("\n== ppy: ", ppy)

    # if (column_is_target):
    #     assert y_pred.shape[0] == ph * (y.shape[0] - ph + 1), (
    #             "\n== y_pred length %d does not match y length (holdout) %d and ph %d"
    #             % (y_pred.shape[0], y.shape[0], ph)
    #     )

    mae, mse, r2, smape, y_pred_avg = [], [], [], [], None
    for i in range(number_targets):  # one TS
        if (column_is_target):
            y1D, y_pred1D = y[:, i].reshape(-1, 1), y_pred[:, i].reshape(-1, 1)
        else:
            y1D, y_pred1D = y[i].reshape(-1, 1), y_pred[i].reshape(-1, 1)

        # reset ph = len(y) if ph was chosen larger than the holdout set
        update_ph = ph
        if update_ph > y1D.shape[0]: update_ph = y1D.shape[0]

        if ppy == "average":
            (mae1D, mse1D, r21D, smape1D, y_pred1D_avg) = __compute_on_one_series(y1D, y_pred1D, update_ph, verbose)
        elif ppy == "original":
            # no averaging from each timestamp, i.e. call sub_func with ph=1
            y_pred1D_avg = y_pred1D
            y1D = prepare_ground_truth(y1D, stepsize=1, prediction_horizon=update_ph)
            (mae1D, mse1D, r21D, smape1D, _) = __compute_on_one_series(y1D.reshape(-1, 1), y_pred1D, ph=1,
                                                                       verbose=verbose)
        else:
            raise (Messages.get_message(message_id='AUTOAITS0072E'))

        if i == 0:
            if (column_is_target):
                mae, mse, r2, smape, y_pred_avg = (
                    [mae1D],
                    [mse1D],
                    [r21D],
                    [smape1D],
                    y_pred1D_avg,
                )
            else:
                y_pred_avg = []
                y_pred_avg.append(y_pred1D_avg)
                mae, mse, r2, smape, y_pred_avg = (
                    [mae1D],
                    [mse1D],
                    [r21D],
                    [smape1D],
                    y_pred_avg,
                )
        else:
            mae.append(mae1D)
            mse.append(mse1D)
            r2.append(r21D)
            smape.append(smape1D)
            if (column_is_target):
                y_pred_avg = np.column_stack((y_pred_avg, y_pred1D_avg))
            else:

                y_pred_avg.append(y_pred1D_avg)

        if number_targets > 1:  # MTS
            # mts might be redundant but being a hot-fix as many other places have used mts field
            mts = {
                "maes": mae,
                "mses": mse,
                "r2s": r2,
                "smapes": smape,
                "y_truth": y,
                "y_pred": y_pred_avg,
                "prediction_horizon": ph,
                "stepsize": 1,
            }
        else:  # UTS
            mts = {}
            mae, mse, r2, smape = mae[0], mse[0], r2[0], smape[0]

    return (mae, mse, r2, smape, y_pred_avg, mts)
