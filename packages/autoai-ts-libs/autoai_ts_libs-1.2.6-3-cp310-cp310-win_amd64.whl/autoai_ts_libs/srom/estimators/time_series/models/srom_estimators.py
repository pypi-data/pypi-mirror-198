################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2020, 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

import copy
import random
import warnings
import time
import numpy as np
import pandas as pd
from typing import List
from random import randint
from sklearn.base import BaseEstimator, RegressorMixin
from autoai_ts_libs.srom.joint_optimizers.auto.base_auto import SROMAuto
from sklearn.model_selection import cross_val_score
from sklearn.utils.validation import check_array
from autoai_ts_libs.srom.transformers.feature_engineering.base import TargetTransformer
from autoai_ts_libs.srom.estimators.regression.auto_ensemble_regressor import (
    SROMEnsemble,
    EnsembleRegressor,
)
from autoai_ts_libs.srom.estimators.utils.time_series import (
    check_model_type_is_dl,
    check_object_is_estimator,
)
from autoai_ts_libs.srom.transformers.preprocessing.ts_transformer import (
    Flatten,
    DifferenceFlatten,
    LocalizedFlatten,
    DifferenceFlattenX,
    LocalizedFlattenX,
    NormalizedFlatten,
    DifferenceNormalizedFlatten,
)
from sklearn.metrics import SCORERS
from joblib import Parallel, delayed
from multiprocessing import cpu_count
from autoai_ts_libs.srom.estimators.utils.time_series import prepare_regressor
from autoai_ts_libs.srom.estimators.utils.time_series import get_optimized_n_jobs
from autoai_ts_libs.utils.messages.messages import Messages
from autoai_ts_libs.utils.score import Score
import time
from autoai_ts_libs.srom.estimators.utils.time_series import get_max_lookback


class SROMTimeSeriesEstimator(BaseEstimator):
    """
    Class which wraps sklearn's pipeline to accomodate transformers
    which modify both X and y. This transformation is required in
    Time Series modelling tasks.
    Parameters
    ----------
        steps (list of tuples): This is the list of tuples storing items
            in the pipeline. For eg.
                steps =  [('anova', SelectKBest(...)),
                            ('svc', SVC(...))]
        feature_columns : (numpy array)
            feature indices
        target_columns : (numpy array)
            target indices
        lookback_win : (int, optional, default = 5)
            Look-back window for the model.
        pred_win : (int, optional, default = 1)
            Look-ahead window for the model.
        time_column : (int, optional, default = -1)
            time column index
        init_time_optimization : (bool, optional)
            does we optimized only at the start of automation
        data_transformation_scheme : (string, optional, default = None)
            data transformation for input and output
        multistep_prediction_strategy : (string)
            multistep prediction strategy recursive or multioutput
        multistep_prediction_win=1 : (int)
            multistep prediction window
        multivariate_column_encoding : (bool,optional)
            enable multivariate column encoding
        store_lookback_history : (bool,optional)
            enable storing of lookback history
    Returns
    -------
        self : object
    """

    def __init__(
        self,
        steps,
        feature_columns,
        target_columns,
        look_ahead_fcolumns=[],
        lookback_win=5,
        pred_win=1,
        time_column=-1,
        init_time_optimization=False,
        data_transformation_scheme=None,
        multistep_prediction_strategy=None,
        multistep_prediction_win=1,
        multivariate_column_encoding=False,
        store_lookback_history=False,
        **kwarg
    ):

        super(SROMTimeSeriesEstimator, self).__init__()

        self.steps = steps
        self.scoring = SCORERS['neg_mean_absolute_error']
        self.cv = None
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.time_column = time_column
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.init_time_optimization = init_time_optimization
        self.data_transformation_scheme = data_transformation_scheme
        self.algorithm = "_" + str(data_transformation_scheme)
        self.multistep_prediction_strategy = multistep_prediction_strategy
        self.multistep_prediction_win = multistep_prediction_win
        self.multivariate_column_encoding = multivariate_column_encoding
        self.store_lookback_history = store_lookback_history

        # adding attr present in sklearn Pipeline. SROM's pipeline utils
        # replies on this attr.
        self.named_steps = self._get_named_steps(self.steps)
        self.transformer_steps = None
        self.is_automate_run = True
        self.look_ahead_fcolumns = look_ahead_fcolumns
        if len(kwarg) > 0:
            if 'estimator' in kwarg.keys():
                self.estimator = kwarg['estimator']
    
    def _get_named_steps(self, steps):
        """
        Adds `named_steps` attr present in sklearn Pipeline.
        SROM's pipeline utils requires this attr.
        Parameters
        ----------
            steps : array of steps

        Returns
        -------
            named steps
        """
        named_steps = {}
        for step in steps:
            named_steps[step[0]] = step[1]
        return named_steps

    def set_scoring(self, scoring):
        """
        Set the scoring mechanism for the SROMTimeSeriesEstimator.
        Parameters
        ----------
            scoring : function or str.
        Returns
        -------
            self : object
        """
        self.scoring = scoring
        return self

    def _multi_variate_col_encoder(self, Xt):
        """
        Internal method for encoder.
        Parameters
        ----------
            Xt : transformed array.

        """
        if len(self.target_columns) > 1 and isinstance(
            self.transformer_steps[0],
            (
                NormalizedFlatten,
                DifferenceNormalizedFlatten,
                LocalizedFlatten,
                DifferenceFlatten,
            ),
        ):
            steps = int(len(Xt) / len(self.target_columns))
            col_mask = np.zeros((len(Xt), len(self.target_columns)))
            for c_step in range(steps):
                start_idx = c_step * len(self.target_columns)
                for col_idx in range(len(self.target_columns)):
                    col_mask[start_idx + col_idx, col_idx] = 1

            Xt = np.hstack((Xt, col_mask))
        return Xt

    def _adjust_indices(self, target_columns: List[int]=[], feature_columns: List[int]=[]):
        """Adjusts feature and target columns as specified by calling the _adjust_indices function 
        (if available) for all the steps in the pipeline. This is intended to be used on
        non-exogenous pipelines so that only the required columns are needed in calls to fit/predict.
        Args:
            target_columns (List[int], optional): New target columns to use. Defaults to [].
            feature_columns (List[int], optional): New feature columns to use. Defaults to [].
        """
        if self.is_exogenous_pipeline_:
            raise RuntimeError("Should not call adjust_indices on an exogenous pipeline")

        self.target_columns = target_columns
        self.feature_columns = feature_columns

        # for all the steps in pipeline call similar adjust function
        for s in self.transformer_steps:
            if hasattr(s, "_adjust_indices") and callable(s._adjust_indices):
                if isinstance(self,(DifferenceFlattenAutoEnsembler,LocalizedFlattenAutoEnsembler)):
                    s._adjust_indices(target_columns=target_columns, feature_columns=target_columns)
                else:
                    s._adjust_indices(target_columns=target_columns, feature_columns=feature_columns)

    def set_cross_validation(self, cv):
        """
        Method to set cross_validation value.
        This is only required when the estimator is AutoSROM
        (AutoRegression and AutoClassification)
        Parameters
        ----------
            cv : int
                no. of folds of crossvalidation for the estimators
        Returns
        -------
            self : object
        """
        self.cv = cv
        return self

    def _input_data_transformation(self, X):
        """
        Internal method for transformation.
        Parameters
        ----------
            X : numpy array.
        """
        # common functions
        def _mean_transform(clm_index, x, operation):
            mean_clm = np.mean(x[:, clm_index], axis=0)
            if operation == "division":
                mean_clm[mean_clm == 0] = 1.0
                x[:, clm_index] = x[:, clm_index] / mean_clm
            elif operation == "substraction":
                x[:, clm_index] = x[:, clm_index] - mean_clm
            return x, mean_clm

        def _get_log_transform(x):
            if x >= 0:
                return np.log(1 + x)
            else:
                return -np.log(-x + 1)

        # automated adjustment in data transformation scheme
        if self.data_transformation_scheme == "auto":
            if sum((X <= 0).any(1)) > 0:
                self.data_transformation_scheme = None
            else:
                self.data_transformation_scheme = "log"

        if self.data_transformation_scheme is None:
            return X

        if isinstance(X, (np.ndarray, np.generic)):
            X = X.copy()
            X = X.astype(float)  # assuming user has not provided integer data
            clm_index = list(set(self.feature_columns + self.target_columns))
            if self.data_transformation_scheme == "log":
                vec_log_fun = np.vectorize(_get_log_transform)
                X[:, clm_index] = vec_log_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "mean_division":
                self.mean_clm_index = clm_index
                X, self.mean_clm = _mean_transform(clm_index, X, "division")
                return X
            elif self.data_transformation_scheme == "mean_substraction":
                self.mean_clm_index = clm_index
                X, self.mean_clm = _mean_transform(clm_index, X, "substraction")
                return X
            elif self.data_transformation_scheme == "mean_division_log":
                vec_log_fun = np.vectorize(_get_log_transform)
                self.mean_clm_index = clm_index
                X, self.mean_clm = _mean_transform(clm_index, X, "division")
                X[:, clm_index] = vec_log_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "mean_substraction_log":
                vec_log_fun = np.vectorize(_get_log_transform)
                self.mean_clm_index = clm_index
                X, self.mean_clm = _mean_transform(clm_index, X, "substraction")
                X[:, clm_index] = vec_log_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "sqrt":
                sqrt_fun = lambda d: np.sqrt(d)
                vec_sqrt_fun = np.vectorize(sqrt_fun)
                X[:, clm_index] = vec_sqrt_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "reciprocal":
                reci_fun = lambda d: np.reciprocal(d + 1)
                vec_reci_fun = np.vectorize(reci_fun)
                X[:, clm_index] = vec_reci_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "anscombe":
                anscombe_fun = lambda d: 2 * np.sqrt(d + 3.0 / 8.0)
                vec_anscombe_fun = np.vectorize(anscombe_fun)
                X[:, clm_index] = vec_anscombe_fun(X[:, clm_index])
                return X
            elif self.data_transformation_scheme == "fisher":
                fisher_fun = lambda d: np.arctanh(np.clip(d, -1 + 1.0e-8, 1.0 - 1.0e-8))
                vec_fisher_fun = np.vectorize(fisher_fun)
                X[:, clm_index] = vec_fisher_fun(X[:, clm_index])
                return X
            else:
                raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0042E"))
        return X

    def _output_data_transformation(self, y):
        """
        This is an internal helper method for transformer.
        Parameters
        ----------
            y : numpy array.
        """
        # common functions

        def _get_inv_log_transform(x):
            if x >= 0:
                return np.exp(x) - 1
            else:
                return 1 - np.exp(-x)

        def inv_mean_transform(y, target_len, mean_clm, mean_clm_index, operation):
            import operator

            if operation == "division":
                op_func = operator.mul
            elif operation == "substraction":
                op_func = operator.add
            if target_len > 1:
                original_shape = y.shape
                y = y.reshape(-1, target_len)
                y = op_func(y, mean_clm[mean_clm_index])
                return y.reshape(original_shape)
            else:
                return op_func(y, mean_clm[mean_clm_index])

        if self.data_transformation_scheme is None:
            return y
        if isinstance(y, (np.ndarray, np.generic)):
            if self.data_transformation_scheme == "log":
                inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
                return inv_vec_log_fun(y)
            elif self.data_transformation_scheme == "mean_division":
                return inv_mean_transform(
                    y,
                    len(self.target_columns),
                    self.mean_clm,
                    self.mean_clm_index,
                    "division",
                )
            elif self.data_transformation_scheme == "mean_substraction":
                return inv_mean_transform(
                    y,
                    len(self.target_columns),
                    self.mean_clm,
                    self.mean_clm_index,
                    "substraction",
                )
            elif self.data_transformation_scheme == "mean_division_log":
                inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
                y = inv_vec_log_fun(y)
                return inv_mean_transform(
                    y,
                    len(self.target_columns),
                    self.mean_clm,
                    self.mean_clm_index,
                    "division",
                )
            elif self.data_transformation_scheme == "mean_substraction_log":
                inv_vec_log_fun = np.vectorize(_get_inv_log_transform)
                y = inv_vec_log_fun(y)
                return inv_mean_transform(
                    y,
                    len(self.target_columns),
                    self.mean_clm,
                    self.mean_clm_index,
                    "substraction",
                )
            elif self.data_transformation_scheme == "sqrt":
                return np.square(y)
            elif self.data_transformation_scheme == "reciprocal":
                return np.reciprocal(y) - 1
            elif self.data_transformation_scheme == "anscombe":
                return np.square(y) / 4.0 + (3.0 / 8.0)
            elif self.data_transformation_scheme == "fisher":
                return np.tanh(y)
            else:
                return y
        return y

    def _validate_steps(self, steps):
        """
        Validate estimator steps.
        Parameters:
        ----------
            steps : estimator steps.
        """
        transformer_steps = [step[1] for step in steps[:-1]]
        estimator = steps[-1][1]

        # check number of tranformers is greater than 0
        if len(transformer_steps) == 0:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0043E"))

        # check if last step is estimator
        if not check_object_is_estimator(estimator):
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0044E"))

    def _data_fit_transform(self, X, y=None):
        """
        Similar to `transform` method in sklearn.pipeline.Pipeline.
        The input and return params of the transformers have been
        modified to incorporate X and y transformation.
        Parameters
        ----------
            X : numpy array.
            y : numpy array.
        """
        Xt = X
        yt = y
        for transformer in self.transformer_steps:
            if hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            else:
                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                Xt = res[0]
                yt = res[1]
            else:
                Xt = res

        return Xt, yt

    def _data_transform(self, X, y=None):
        """
        Transform method.
        Parameters
        ----------
            X : numpy array.
            y : numpy array.

        """
        Xt = X
        yt = y
        for transformer in self.transformer_steps:
            res = transformer.transform(Xt)

            if isinstance(res, tuple):
                Xt = res[0]
                yt = res[1]
            else:
                Xt = res

        return Xt, yt

    def _init_transformer_and_estimator(self):
        """
        Init method for transformer and estimator.
        """
        self._validate_steps(self.steps)
        self.transformer_steps = [step[1] for step in self.steps[:-1]]
        if not self.init_time_optimization or not self.is_automate_run:
            self.estimator = self.steps[-1][1]

    def _store_lookback_history_X(self, X):
        """
        Store history.
        Parameters
        ----------
            X : numpy array.

        """
        if self.store_lookback_history:
            max_lookback = get_max_lookback(self.lookback_win)
            if max_lookback > 0:
                self.lookback_data_X = X[(X.shape[0] - max_lookback) :, :]
                if self.look_ahead_fcolumns!=None:
                    if len(self.look_ahead_fcolumns)>0:
                        self.look_ahead_mean = np.nanmean(self.lookback_data_X[:,self.look_ahead_fcolumns],axis=0)
                        self.look_ahead_mean = self.look_ahead_mean.reshape(-1,len(self.look_ahead_fcolumns))
                        self.look_ahead_mean = np.repeat(self.look_ahead_mean,self.pred_win, axis=0)

            else:
                self.lookback_data_X = None
        else:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0045E"))

    def _add_lookback_history_to_X(self, X):
        """
        Add history.
        Parameters
        ----------
            X : numpy array.
        """
        if self.store_lookback_history:
            max_lookback = get_max_lookback(self.lookback_win)
            if X is None:
                if max_lookback > 0:
                    return self.lookback_data_X.copy()
                else:
                    return X
            else:
                if max_lookback > 0:
                    try:
                        new_X = np.concatenate([self.lookback_data_X, X])
                    except Exception as e:
                        raise Exception(
                            Messages.get_message(str(e), message_id="AUTOAITSLIBS0055E")
                        )
                    return new_X
                else:
                    return X
        else:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0045E"))

    def _display_transformations(self, X, y=None):
        """
        This method is for testing transformations.
        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            y : array-like of shape (n_samples,)
                The target values.

        Returns
        -------
            self : object
        """
        X = self._input_data_transformation(X)

        #self._init_transformer_and_estimator()

        Xt, yt = self._data_fit_transform(X, y)
        
        return Xt, yt
    
    def fit(self, X, y=None):
        """
        Similar to `fit` method in sklearn.pipeline.Pipeline.
        The input and return params of the transformers have been
        modified to incorporate X and y transformation.

        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            y : array-like of shape (n_samples,)
                The target values.

        Returns
        -------
            self : object
        """
        # this is new addition, as we will store the lookback
        # this will only if Flag is enabled
        # this will help to preserve the old style
        if self.store_lookback_history:
            self._store_lookback_history_X(X)

        # this is newly added steps
        X = self._input_data_transformation(X)

        # internally initializing the transformer_steps and estimators.
        self._init_transformer_and_estimator()

        # transforming the data from the list of transformers and getting data shape.
        pre_shape = X.shape
        Xt, yt = self._data_fit_transform(X, y)

        if self.multivariate_column_encoding:
            Xt = self._multi_variate_col_encoder(Xt)

        post_shape = Xt.shape

        # cross validator object
        if self.cv is None:
            from autoai_ts_libs.srom.joint_optimizers.cv.time_series_splits import (
                TimeSeriesTrainTestSplit,
            )

            validation_part = 0.3
            self.cv = TimeSeriesTrainTestSplit(
                n_test_size=(int(validation_part * (len(Xt))))
            )

        #  The model params will
        # automatically  be updated for input dimension in the case of DL models.
        # The models considered as Deep Learning are in the list
        # MODEL_TYPES_SUPPORTED_FOR_DEEP_LEARNING
        # update train pipelines with params
        if hasattr(self.estimator, "set_params") and callable(
            getattr(self.estimator, "set_params")
        ):
            if (
                "input_dimension" in self.estimator.get_params()
                and check_model_type_is_dl(self.estimator)
            ):

                # get estimator input dim
                in_dim = self.estimator.get_params()["input_dimension"]
                if len(in_dim) > 1:
                    # in case of models where input shape is defined like (6,10) (keras)
                    new_in_dim = (post_shape[1], in_dim[1])
                else:
                    # in case of models where input shape is defined like (6,) (keras)
                    new_in_dim = (post_shape[1],)
                self.estimator.set_params(input_dimension=new_in_dim)
            else:
                pass

        self.estimator.fit(Xt, yt)

        # set it was runned
        self.is_automate_run = True

        return self

    def predict_sliding_window(self, X):
        """
        This is an in-sample prediction.
        Given a data of X, it will slide a window and make single prediction.
        Output will match the size of predict
        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.

        Returns
        -------
            self : object
        """
        y = self._predict(X)
        return y.reshape(-1, len(self.target_columns))

    def _add_exogenous_to_X(self, X, exogenous):
        """ """
        if len(exogenous.shape) == 1:
            exogenous = exogenous.reshape(-1, 1)
        assert self.pred_win == len(
            exogenous
        ), "number of rows in exogenous cols should match with pred win."
        assert (
            len(self.look_ahead_fcolumns) == exogenous.shape[1]
        ), "exogenous cols not in proper format."
        newX = np.full((self.pred_win, X.shape[1]), np.nan)
        for idx, val in enumerate(self.look_ahead_fcolumns):
            newX[:, val] = exogenous[:, idx]
        X = np.vstack((X, newX))
        return X

    def __str__(self):
        str_rep = str(self.__class__.__name__)
        str_rep = str_rep + '('
        for key,val in sorted(self.get_params().items()):
            if key not in ["estimator"]:
                str_rep = str_rep + str(key) + '=' + str(val) + ',\n\t\t\t\t'
        str_rep = str_rep.rstrip(',\n\t\t\t\t') 
        str_rep = str_rep + ')'
        return str_rep
    
    def _recursive_predict_helper(self, X):
        """
        This is an internal helper method used for by recusrsive prediction strategy.
        Parameters
        ----------
            X : Input array.
        Returns
        -------
            self : numpy array.
        """
        max_lookback = get_max_lookback(self.lookback_win)

        if (
            hasattr(self, "is_recursive_multi_step_sliding")
            and self.is_recursive_multi_step_sliding == True
        ):
            # This is a check to identify if method is called from predict or predict_multi_step_sliding_window
            y_pred = self.predict_sliding_window(X)
            return y_pred[
                max_lookback:,
            ]
        else:
            preds = []
            for step in range(self.multistep_prediction_win):
                pred = self.predict_sliding_window(X)
                pred = pred[
                    max_lookback:,
                ]
                X = X[
                    1:max_lookback,
                ]
                new_row = np.zeros((1, X.shape[1]))
                np.put(new_row, self.target_columns, pred)
                X = np.concatenate((X, new_row))
                dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                X = np.concatenate((X, dummy))
                if step == 0:
                    preds = pred
                else:
                    preds = np.concatenate((preds, pred))
            preds = preds.flatten().reshape(-1, len(self.target_columns))
            return preds

    def predict(self, X=None, supporting_features=None, prediction_type=None):
        """
        Returns the prediction.
        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            prediction_type : It can be sliding_window or forecast. Default is forecast.
        Returns
        -------
            y_pred : ndarray of shape (n_samples,)
                The predicted values.
        """
        if isinstance(supporting_features, np.matrix):
            supporting_features = np.squeeze(np.asarray(supporting_features))
        
        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            max_lookback = get_max_lookback(self.lookback_win)
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            max_lookback = self.lookback_win
        
        if X is not None:
            X = check_array(X, dtype=np.float64, force_all_finite=False, ensure_2d=False, ensure_min_samples=0)
            if np.count_nonzero(np.isnan(X)) > 0:
                raise Exception(Messages.get_message(message_id='AUTOAITSLIBS0067E'))

        if prediction_type is not None:
            if prediction_type.lower() == Score.PREDICT_SLIDING_WINDOW:
                if self.pred_win == 1:
                    return self.predict_sliding_window(X)
                elif self.pred_win > 1:
                    return self.predict_multi_step_sliding_window(X)
                else:
                    raise Exception(
                        Messages.get_message(
                            prediction_type, message_id="AUTOAITSLIBS0046E"
                        )
                    )
            elif prediction_type.lower() != Score.PREDICT_FORECAST:
                raise Exception(
                    Messages.get_message(
                        prediction_type, message_id="AUTOAITSLIBS0046E"
                    )
                )
        # we know
        if self.store_lookback_history:
            X = self._add_lookback_history_to_X(X)

        if (X.shape[0] - max_lookback) < 0:
            raise Exception(
                Messages.get_message(
                    format(max_lookback),
                    format(X.shape[0]),
                    message_id="AUTOAITSLIBS0047E",
                )
            )

        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            if len(self.look_ahead_fcolumns) <= 0:
                # we shd raise error
                X = X[
                    (X.shape[0] - max_lookback) :,
                ]
                if self.pred_win > 0:
                    if self.multistep_prediction_strategy == "recursive":
                        dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    else:
                        dummy = np.full((self.multistep_prediction_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))
            else:
                if not supporting_features is None:
                    X = self._add_exogenous_to_X(X, supporting_features)
                else:
                    X = self._add_exogenous_to_X(X, self.look_ahead_mean)                
                X = X[
                    (X.shape[0] - (max_lookback + self.pred_win)) :,
                ]
                X[np.isnan(X)] = 0.0
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            X = X[(X.shape[0] - self.lookback_win) :,]
            if self.pred_win > 0:
                if self.multistep_prediction_strategy == "recursive":
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                else:
                    dummy = np.full((self.multistep_prediction_win, X.shape[1]), 0.0)
                X = np.concatenate((X, dummy))

        
        if self.multistep_prediction_win == 1:
            y_pred = self.predict_sliding_window(X)
    

            # Remove None padding
            if self.pred_win == 0:
                return y_pred[
                    max_lookback - 1 :,
                ]
            else:
                return y_pred[
                    max_lookback:,
                ]
        elif self.pred_win == 1 and self.multistep_prediction_strategy == "recursive":
            return self._recursive_predict_helper(X)
        else:
            y_pred = self.predict_multi_step_sliding_window(X)
            # fix for consistency in output
            y_pred = y_pred.reshape(-1, len(self.target_columns))
    
            return y_pred

    def _predict(self, X, num_predictions=-1):
        """
        This is an internal helper method used in predict.
        Parameters
        ----------
            X: {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            num_predictions: The number of samples to predict in the data
                from the end. If the value is 0 or -1, the method will return
                as many predictions as possible. The rest of the values are padded
                with null values.
        Returns
        -------
            y_pred : ndarray of shape (n_samples,)
                The predicted values
        """

        num_samples_in_input = X.shape[0]

        # this is newly added steps
        X = self._input_data_transformation(X)

        Xt, _ = self._data_transform(X, y=None)
        if self.multivariate_column_encoding:
            Xt = self._multi_variate_col_encoder(Xt)
        y_pred = self.estimator.predict(Xt)

        if self.pred_win == 1:
            y_pred = y_pred.reshape(-1, len(self.target_columns))
            if isinstance(self.transformer_steps[0], TargetTransformer):
                y_pred = self.transformer_steps[0].inverse_transform(y_pred)
                y_pred = y_pred.reshape(-1, len(self.target_columns))
        else:
            if isinstance(self.transformer_steps[0], TargetTransformer):
                y_pred = self.transformer_steps[0].inverse_transform(y_pred)
                ### Backward compatibility 1258
                ###
                ### Code with exogenous support
                if self.look_ahead_fcolumns!=None:
                    imp_lst = (
                        NormalizedFlatten,
                        DifferenceNormalizedFlatten,
                        LocalizedFlatten,
                        DifferenceFlatten,
                        LocalizedFlattenX,
                        DifferenceFlattenX,
                    )
                else:
                ### Backward compatibility 1258
                ###
                ### Code prior to exogenous support    
                    imp_lst = (
                        NormalizedFlatten,
                        DifferenceNormalizedFlatten,
                        LocalizedFlatten,
                        DifferenceFlatten
                    )
                if isinstance(
                    self.transformer_steps[0],
                    imp_lst,
                ):
                    # y_pred = y_pred.reshape(-1, self.pred_win)
                    _c = []
                    c_steps = int(len(y_pred) / len(self.target_columns))
                    for c_step in range(c_steps):
                        start_idx = c_step * len(self.target_columns)
                        end_idx = start_idx + len(self.target_columns)
                        col_pred = y_pred[start_idx:end_idx]
                        row_pred = np.transpose(col_pred)
                        _c.append(row_pred.flatten())
                    y_pred = np.array(_c)
        y_pred = self._output_data_transformation(y_pred)

        y_pred[np.isinf(y_pred)] = None

        if self.pred_win == 1:
            if len(y_pred.shape) == 1:
                # y_pred is 1-D array
                n_steps_ahead = 1
                null_padding = np.array(
                    [None for i in range(int(num_samples_in_input))]
                )

            else:
                # y_pred is 2-D array
                n_steps_ahead = y_pred.shape[1]
                null_padding = np.array(
                    [
                        [None for i in range(n_steps_ahead)]
                        for j in range(int(num_samples_in_input))
                    ]
                )

            if num_predictions > 0:
                return np.concatenate(
                    [null_padding[:-num_predictions], y_pred[-num_predictions:]]
                )
            else:
                # if num_predictions = 0, -1; return all possible predictions
                return np.concatenate([null_padding[: -len(y_pred)], y_pred])
        else:
            return y_pred

    def score(self, X, y=None, sample_weight=None):
        """
        Similar to `score` method in sklearn.pipeline.Pipeline.
        The input and return params of the transformers have been modified
        to incorporate X and y transformation.
        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            y : array-like of shape (n_samples,)
                The target values (class labels in classification, real numbers in
                regression).
            sample_weight : array-like of shape (n_samples,), default=None
                Sample weights. If None, then samples are equally weighted.
                Note that this is supported only if the base estimator supports
                sample weighting.
        Returns
        -------
            score : float
        """

        # this is newly added steps
        X = self._input_data_transformation(X)
        Xt, yt = self._data_transform(X, y=y)
        yt = self._output_data_transformation(yt)

        score_params = {}
        if sample_weight is not None:
            score_params["sample_weight"] = sample_weight

        return self.scoring(self.estimator, Xt, yt)
        # print(yt, self.steps[-1][-1].predict(Xt))
        # return self.scoring(yt, self.steps[-1][-1].predict(Xt))

    def get_params(self, deep=True):
        """
        Get parameters for this estimator.
        Parameters
        ----------
            deep : boolean, optional
                If True, will return the parameters for this estimator and
                contained subobjects that are estimators.
        Returns
        -------
            params : mapping of string to any
                Parameter names mapped to their values.

        """
        out = super().get_params(deep=deep)
        if not deep:
            return out
        estimators = getattr(self, "steps")
        for name, estimator in estimators:
            if hasattr(estimator, "get_params"):
                for key, value in estimator.get_params(deep=True).items():
                    out["%s__%s" % (name, key)] = value

        return out

    def set_params(self, attr="steps", **params):
        """
        Set the parameters of this estimator.
        Parameters
        ----------
            attrs : str
            params : map of parameters

        """
        temp_params = copy.deepcopy(params)
        for step in self.steps:
            est_params = {}
            for param in params:
                prefix = step[0] + "__"
                if param.startswith(prefix):
                    est_params[param.split(prefix)[1]] = temp_params.pop(param)

            step[1].set_params(**est_params)

        for param in params:
            if param.startswith("lookback_win"):
                self.steps[0][1].set_params(**{"lookback_win": params[param]})

        for param in temp_params:
            setattr(self, param, temp_params[param])

        return self

    def predit_recursive_multi_step(self, X):
        """
        Predict multiple steps
        Parameters
        ----------
            X : numpy array.
        Returns
        -------
            y : numpy array
        """
        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            max_lookback = get_max_lookback(self.lookback_win)
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            max_lookback = self.lookback_win

        if X.shape[0] != max_lookback:
            raise Exception(
                Messages.get_message(
                    format(max_lookback),
                    format(X.shape[0]),
                    message_id="AUTOAITSLIBS0048E",
                )
            )

        if self.pred_win != 1:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0049E"))

        if self.multistep_prediction_win == 1:
            return self.predict(X)

        if self.feature_columns != self.target_columns:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0050E"))

        if self.multistep_prediction_win > 1:
            # iteratively call predict
            # we assume shape of predict call's output and X is same.
            # we can append the output
            tmp_X = X.copy()
            for current_step in range(self.multistep_prediction_win):
                current_step_forcast = self.predict(tmp_X)
                # to go to next step, we need
                # append output of predict to tmp_X and also remove first records from tmp_X
                # above step will make sure that tmp_X is of same size as X.
                new_row = np.zeros((1, tmp_X.shape[1]))
                np.put(new_row, self.target_columns, current_step_forcast)
                tmp_X = tmp_X[
                    1:,
                ]
                tmp_X = np.append(tmp_X, new_row, axis=0)
                if current_step == 0:
                    current_step_forcast_all = current_step_forcast
                else:
                    current_step_forcast_all = np.concatenate(
                        (current_step_forcast_all, current_step_forcast), axis=0
                    )
        return current_step_forcast_all

    def _use_parallel_version_of_multi_step_sliding_window(self, X):
        """
        This is an internal helper method used in predict.
        Parameters
        ----------
            X: {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
        """
        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            max_lookback = get_max_lookback(self.lookback_win)
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            max_lookback = self.lookback_win

        _X = [
            X[
                i - max_lookback : i,
            ]
            for i in range(max_lookback, X.shape[0] - self.multistep_prediction_win + 1)
        ]
        ans = Parallel(n_jobs=cpu_count() - 1)(
            delayed(self.predit_recursive_multi_step)(item) for item in _X
        )
        ans = [item.flatten() for item in ans]
        return pd.DataFrame(ans).values

    def _use_multioutput_version_of_multi_step_sliding_window(self, X):
        """
        This is an internal helper method used in predict.
        Parameters
        ----------
            X: {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
        """
        y = self._predict(X)
        return y.reshape(-1, len(self.target_columns))

    def predict_multi_step_sliding_window(self, X):
        """
        Predict multiple steps in a sliding window.
        Parameters
        ----------
            X : numpy array.
        Returns
        -------
            y : numpy array
        """
        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            max_lookback = get_max_lookback(self.lookback_win)
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            max_lookback = self.lookback_win
        if max_lookback > 0:
            if self.multistep_prediction_strategy == "recursive":
                self.is_recursive_multi_step_sliding = True
                result = self._use_parallel_version_of_multi_step_sliding_window(X)
                result = result.reshape(-1, len(self.target_columns))
                self.is_recursive_multi_step_sliding = False
                return result

            elif self.multistep_prediction_strategy == "multioutput":
                return self._use_multioutput_version_of_multi_step_sliding_window(X)

        raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0051E"))

    def _transformer_helper(self, y_pred):
        """
        This is an internal helper method for transformer.
        Parameters
        ----------
            y_pred : numpy array

        """
        _c = []
        c_steps = int(len(y_pred) / len(self.target_columns))
        for c_step in range(c_steps):
            start_idx = c_step * len(self.target_columns)
            end_idx = start_idx + len(self.target_columns)
            col_pred = y_pred[start_idx:end_idx]
            row_pred = np.transpose(col_pred)
            _c.append(row_pred.flatten())
        return np.array(_c)

    def _recursive_predict_proba_helper(self, X):
        """
        This is an internal helper method for predict prob function.
        Parameters
        ----------
            X : numpy array
        """
        ### Backward compatibility 1258
        ###
        ### Code with exogenous support
        if self.look_ahead_fcolumns!=None:
            max_lookback = get_max_lookback(self.lookback_win)
        else:
        ### Backward compatibility 1258
        ###
        ### Code prior to exogenous support
            max_lookback = self.lookback_win
        predictions = self.predict(X)
        predictions = predictions.reshape(-1, len(self.target_columns))
        for step in range(self.multistep_prediction_win):
            if step == 0:
                pred_probs = self.predict_proba(X)
            else:
                if self.recursive_cnt > 0:
                    pre_pred = predictions[step - 1]
                    X = X[
                        1:max_lookback,
                    ]
                    new_row = np.zeros((1, X.shape[1]))
                    np.put(new_row, self.target_columns, pre_pred)
                    X = np.concatenate((X, new_row))
                    pred_probs = np.concatenate((pred_probs, self.predict_proba(X)))
        return pred_probs

    def predict_proba(self, X):
        """
        Prediction probability
        Parameters
        ----------
            X : numpy array.
        Returns
        -------
            y : numpy array
        """
        if isinstance(self.estimator, (EnsembleRegressor)):
            if self.pred_win > 0:
                if self.multistep_prediction_strategy == "recursive":
                    if hasattr(self, "recursive_cnt"):
                        self.recursive_cnt = self.recursive_cnt - 1
                        dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    else:
                        self.recursive_cnt = self.multistep_prediction_win
                        predict_probs = self._recursive_predict_proba_helper(X)
                        delattr(self, "recursive_cnt")
                        return predict_probs
                else:
                    dummy = np.full((self.multistep_prediction_win, X.shape[1]), 0.0)
                X = np.concatenate((X, dummy))
            X = self._input_data_transformation(X)
            Xt, _ = self._data_transform(X, y=None)
            try:
                yt = self.estimator.predict_proba(Xt)
                yt = yt.transpose()
                lower = yt[0]
                upper = yt[1]
                if self.pred_win > 1:
                    if isinstance(self.transformer_steps[0], TargetTransformer):
                        lower = self.transformer_steps[0].inverse_transform(lower)
                        upper = self.transformer_steps[0].inverse_transform(upper)
                        if isinstance(
                            self.transformer_steps[0],
                            (
                                NormalizedFlatten,
                                DifferenceNormalizedFlatten,
                                LocalizedFlatten,
                                DifferenceFlatten,
                            ),
                        ):
                            lower = self._transformer_helper(lower)
                            upper = self._transformer_helper(upper)
                else:
                    if (len(self.target_columns) == 1) and (len(lower.shape) == 1):
                        lower = lower.reshape(-1, 1)
                        upper = upper.reshape(-1, 1)
                    if isinstance(self.transformer_steps[0], TargetTransformer):
                        lower = self.transformer_steps[0].inverse_transform(lower)
                        lower = lower.reshape(-1, len(self.target_columns))
                        upper = self.transformer_steps[0].inverse_transform(upper)
                        upper = upper.reshape(-1, len(self.target_columns))
                low_pred_yt = self._output_data_transformation(lower)
                upper_pred_yt = self._output_data_transformation(upper)
                return np.array([low_pred_yt, upper_pred_yt]).transpose()
            except:
                raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0052E"))
        else:
            raise Exception(Messages.get_message(message_id="AUTOAITSLIBS0053E"))

    def _reset_fc_cols_and_lookback(
        self, feature_columns, target_columns, lookback_win, pred_win
    ):
        """ """
        look_ahead_fc_cols = []
        fc_cols = []
        new_lookback_win = []
        if isinstance(lookback_win, list):
            for idx, item in enumerate(lookback_win):
                if item < 0:
                    assert (
                        not feature_columns[idx] in target_columns
                    ), "feature col should not be part of target col."
                    look_ahead_fc_cols.append(feature_columns[idx])
                else:
                    fc_cols.append(feature_columns[idx])
                    new_lookback_win.append(item)
            feature_columns = fc_cols
            lookback_win = new_lookback_win
        return feature_columns, lookback_win, look_ahead_fc_cols


    def get_params(self, deep=True):
        ans = super().get_params(deep=deep)
        ans['estimator'] = self.estimator
        return ans

    @property
    def is_exogenous_pipeline_(self):
        """"""
        if self.look_ahead_fcolumns!=None:
            if len(self.look_ahead_fcolumns)==0 and set(self.feature_columns) == set(self.target_columns) and len(self.feature_columns)> 0:
                return False
            else:
                return True
        return False

    @property
    def is_future_exogenous_pipeline_(self):
        """"""
        if self.is_exogenous_pipeline_:
            if len(self.look_ahead_fcolumns)>0:
                return True
        return False

    def __setstate__(self, state):
        super().__setstate__(state)
        if not hasattr(self, "look_ahead_fcolumns"):
            self.look_ahead_fcolumns = None
        
class FlattenAutoEnsembler(SROMTimeSeriesEstimator):
    """
    SROM transformation wrapper class for Flatten
    transformer and auto ensembler (estimator)
    Parameters
    ----------
        feature_columns : (numpy array)
            feature indices
        target_columns : (numpy array)
            target indices
        lookback_win : (int, optional)
            Look-back window for the model.
        pred_win : (int)
            Look-ahead window for the model.
        time_column:(int)
            time-column index
        init_time_optimization : (bool, optional)
            does we optimized only at the start.
        data_transformation_scheme : (string, optional, default = None)
            data transformation for input and output
        total_execution_time : (int, optional)
            (approximate) maximum runtime allowed.
        execution_time_per_pipeline : (number, optional)
            maximum execution time per pipeline allowed.
        dag_granularity : (string, optional)
            granularity for execution. Values can be default or tiny.
        execution_platform : (string)
            Platform for execution from srom pipeline. Supports spark also.
        ensemble_type : (string)
            It can be voting or stacked.
        store_lookback_history : (bool,optional)
            enable storing of lookback history
        n_jobs : (int)
            no of jobs

    """

    def __init__(
        self,
        feature_columns,
        target_columns,
        lookback_win,
        pred_win,
        time_column=-1,
        init_time_optimization=False,
        data_transformation_scheme=None,
        total_execution_time=2,
        execution_time_per_pipeline=1,
        dag_granularity="default",
        execution_platform="spark_node_random_search",
        n_leaders_for_ensemble=5,
        n_estimators_for_pred_interval=30,
        max_samples_for_pred_interval=1.0,
        multistep_prediction_strategy=None,
        multistep_prediction_win=1,
        ensemble_type="voting",
        store_lookback_history=False,
        n_jobs = -1,
        look_ahead_fcolumns = [],
        **kwarg
    ):
        self.dag_granularity = dag_granularity
        self.execution_platform = execution_platform
        self.execution_time_per_pipeline = execution_time_per_pipeline
        self.total_execution_time = total_execution_time
        self.n_leaders_for_ensemble = n_leaders_for_ensemble
        self.n_estimators_for_pred_interval = n_estimators_for_pred_interval
        self.max_samples_for_pred_interval = max_samples_for_pred_interval
        self.ensemble_type = ensemble_type
        self.store_lookback_history = store_lookback_history
        self.n_jobs = get_optimized_n_jobs(
            n_jobs=n_jobs, no_outputs=len(target_columns) * pred_win
        )

        
        if len(target_columns) >= 20 and pred_win >= 100:
            self.execution_time_per_pipeline = self.execution_time_per_pipeline * 2
            self.total_execution_time = self.total_execution_time * 2

        flatten = (
            "Flatten",
            Flatten(
                feature_col_index=feature_columns,
                target_col_index=target_columns,
                lookback_win=lookback_win,
                pred_win=pred_win,
                look_ahead_fcol_index=look_ahead_fcolumns,
            ),
        )

        auto_reg = prepare_regressor(
            dag_granularity=dag_granularity,
            total_execution_time=self.total_execution_time,
            execution_time_per_pipeline=self.execution_time_per_pipeline,
            r_type="AutoEnsemble",
            execution_platform=execution_platform,
            n_leaders_for_ensemble=n_leaders_for_ensemble,
            n_estimators_for_pred_interval=n_estimators_for_pred_interval,
            max_samples_for_pred_interval=max_samples_for_pred_interval,
            ensemble_type=ensemble_type,
            n_jobs=self.n_jobs,
        )

        steps = [flatten, auto_reg]

        super(FlattenAutoEnsembler, self).__init__(
            steps=steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            look_ahead_fcolumns=look_ahead_fcolumns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            init_time_optimization=init_time_optimization,
            data_transformation_scheme=data_transformation_scheme,
            multistep_prediction_strategy=multistep_prediction_strategy,
            multistep_prediction_win=multistep_prediction_win,
            store_lookback_history=store_lookback_history,
            **kwarg
        )

    def set_params(self, attr="steps", **params):
        super(FlattenAutoEnsembler, self).set_params(**params)

    def name(self):
        return "FlattenAutoEnsembler"


class DifferenceFlattenAutoEnsembler(SROMTimeSeriesEstimator):
    """
    SROM transformation wrapper class for Flatten
    transformer and auto regression (estimator)

    Parameters
    ----------
        feature_columns : (numpy array)
            feature indices
        target_columns : (numpy array)
            target indices
        lookback_win : (int, optional)
            Look-back window for the model.
        pred_win : (int)
            Look-ahead window for the model.
        time_column:(int)
            time-column index
        init_time_optimization : (bool, optional)
            does we optimized only at the start.
        data_transformation_scheme : (string, optional, default = None)
            data transformation for input and output
        total_execution_time : (int, optional)
            (approximate) maximum runtime allowed.
        execution_time_per_pipeline : (number, optional)
            maximum execution time per pipeline allowed.
        dag_granularity : (string, optional)
            granularity for execution. Values can be default or tiny.
        execution_platform : (string)
            Platform for execution from srom pipeline. Supports spark also.
        ensemble_type : (string)
            It can be voting or stacked.
        multivariate_column_encoding : (boolean)
            enable multivariate_column_encoding
            It can be voting or stacked.
        store_lookback_history : (bool,optional)
            enable storing of lookback history
        n_jobs : (int)
            no of jobs

    """

    def __init__(
        self,
        feature_columns,
        target_columns,
        lookback_win,
        pred_win,
        time_column=-1,
        init_time_optimization=False,
        data_transformation_scheme=None,
        total_execution_time=2,
        execution_time_per_pipeline=1,
        dag_granularity="default",
        execution_platform="spark_node_random_search",
        n_leaders_for_ensemble=5,
        n_estimators_for_pred_interval=30,
        max_samples_for_pred_interval=1.0,
        multistep_prediction_strategy=None,
        multistep_prediction_win=1,
        ensemble_type="voting",
        multivariate_column_encoding=False,
        store_lookback_history=False,
        n_jobs=-1,
        look_ahead_fcolumns = [],
        **kwarg
    ):
        self.dag_granularity = dag_granularity
        self.execution_platform = execution_platform
        self.execution_time_per_pipeline = execution_time_per_pipeline
        self.total_execution_time = total_execution_time
        self.n_leaders_for_ensemble = n_leaders_for_ensemble
        self.n_estimators_for_pred_interval = n_estimators_for_pred_interval
        self.max_samples_for_pred_interval = max_samples_for_pred_interval
        self.ensemble_type = ensemble_type
        self.store_lookback_history = store_lookback_history
        self.n_jobs = get_optimized_n_jobs(n_jobs=n_jobs, no_outputs=pred_win)

        if (look_ahead_fcolumns is not None and len(look_ahead_fcolumns) > 0 and len(feature_columns) == len(target_columns)) or len(feature_columns) != len(target_columns) or set(feature_columns) != set(
            target_columns
        ):
            flatten = (
                "DifferenceFlatten",
                DifferenceFlattenX(
                    feature_col_index=feature_columns,
                    target_col_index=target_columns,
                    lookback_win=lookback_win,
                    pred_win=pred_win,
                    look_ahead_fcol_index=look_ahead_fcolumns,
                ),
            )
        else:
            flatten = (
                "DifferenceFlatten",
                DifferenceFlatten(
                    feature_col_index=feature_columns,
                    target_col_index=target_columns,
                    lookback_win=lookback_win,
                    pred_win=pred_win,
                ),
            )
        auto_reg = prepare_regressor(
            dag_granularity=dag_granularity,
            total_execution_time=total_execution_time,
            execution_time_per_pipeline=execution_time_per_pipeline,
            r_type="AutoEnsemble",
            execution_platform=execution_platform,
            n_leaders_for_ensemble=n_leaders_for_ensemble,
            n_estimators_for_pred_interval=n_estimators_for_pred_interval,
            max_samples_for_pred_interval=max_samples_for_pred_interval,
            ensemble_type=ensemble_type,
            n_jobs=self.n_jobs,
        )

        steps = [flatten, auto_reg]

        super(DifferenceFlattenAutoEnsembler, self).__init__(
            steps=steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            look_ahead_fcolumns=look_ahead_fcolumns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            init_time_optimization=init_time_optimization,
            data_transformation_scheme=data_transformation_scheme,
            multistep_prediction_strategy=multistep_prediction_strategy,
            multistep_prediction_win=multistep_prediction_win,
            multivariate_column_encoding=multivariate_column_encoding,
            store_lookback_history=store_lookback_history,
            **kwarg
        )

    def set_params(self, attr="steps", **params):
        super(DifferenceFlattenAutoEnsembler, self).set_params(**params)

    def name(self):
        return "DifferenceFlattenAutoEnsembler"



class LocalizedFlattenAutoEnsembler(SROMTimeSeriesEstimator):
    """
    SROM transformation wrapper class for Flatten
    transformer and auto ensembler (estimator)
    Parameters
    ----------
        feature_columns : (numpy array)
            feature indices
        target_columns : (numpy array)
            target indices
        lookback_win : (int, optional)
            Look-back window for the model.
        pred_win : (int)
            Look-ahead window for the model.
        time_column:(int)
            time-column index
        init_time_optimization : (bool, optional)
            does we optimized only at the start.
        data_transformation_scheme : (string, optional, default = None)
            data transformation for input and output
        total_execution_time : (int, optional)
            (approximate) maximum runtime allowed.
        execution_time_per_pipeline : (number, optional)
            maximum execution time per pipeline allowed.
        dag_granularity : (string, optional)
            granularity for execution. Values can be default or tiny.
        execution_platform : (string)
            Platform for execution from srom pipeline. Supports spark also.
        ensemble_type : (string)
            It can be voting or stacked.
        multivariate_column_encoding : (boolean)
            enable multivariate_column_encoding
        store_lookback_history : (bool,optional)
            enable storing of lookback history
        n_jobs : (int)
            no of jobs

    """

    def __init__(
        self,
        feature_columns,
        target_columns,
        lookback_win,
        pred_win,
        time_column=-1,
        init_time_optimization=False,
        data_transformation_scheme=None,
        total_execution_time=2,
        execution_time_per_pipeline=1,
        dag_granularity="default",
        execution_platform="spark_node_random_search",
        n_leaders_for_ensemble=5,
        n_estimators_for_pred_interval=30,
        max_samples_for_pred_interval=1.0,
        multistep_prediction_strategy=None,
        multistep_prediction_win=1,
        ensemble_type="voting",
        multivariate_column_encoding=False,
        store_lookback_history=False,
        n_jobs=-1,
        look_ahead_fcolumns = [],
        **kwarg
    ):
        self.dag_granularity = dag_granularity
        self.total_execution_time = total_execution_time
        self.execution_time_per_pipeline = execution_time_per_pipeline
        self.execution_platform = execution_platform
        self.n_leaders_for_ensemble = n_leaders_for_ensemble
        self.n_estimators_for_pred_interval = n_estimators_for_pred_interval
        self.max_samples_for_pred_interval = max_samples_for_pred_interval
        self.ensemble_type = ensemble_type
        self.store_lookback_history = store_lookback_history
        self.n_jobs = get_optimized_n_jobs(n_jobs=n_jobs, no_outputs=pred_win)

        if (look_ahead_fcolumns is not None and len(look_ahead_fcolumns) > 0 and len(feature_columns) == len(target_columns)) or len(feature_columns) != len(target_columns) or set(feature_columns) != set(
            target_columns
        ):
            flatten = (
                "LocalizedFlatten",
                LocalizedFlattenX(
                    feature_col_index=feature_columns,
                    target_col_index=target_columns,
                    lookback_win=lookback_win,
                    pred_win=pred_win,
                    look_ahead_fcol_index=look_ahead_fcolumns,
                ),
            )
        else:
            flatten = (
                "LocalizedFlatten",
                LocalizedFlatten(
                    feature_col_index=feature_columns,
                    target_col_index=target_columns,
                    lookback_win=lookback_win,
                    pred_win=pred_win,
                ),
            )

        auto_reg = prepare_regressor(
            dag_granularity=dag_granularity,
            total_execution_time=total_execution_time,
            execution_time_per_pipeline=execution_time_per_pipeline,
            r_type="AutoEnsemble",
            execution_platform=execution_platform,
            n_leaders_for_ensemble=n_leaders_for_ensemble,
            n_estimators_for_pred_interval=n_estimators_for_pred_interval,
            max_samples_for_pred_interval=max_samples_for_pred_interval,
            ensemble_type=ensemble_type,
            n_jobs=self.n_jobs,
        )

        steps = [flatten, auto_reg]

        super(LocalizedFlattenAutoEnsembler, self).__init__(
            steps=steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            look_ahead_fcolumns=look_ahead_fcolumns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            init_time_optimization=init_time_optimization,
            data_transformation_scheme=data_transformation_scheme,
            multistep_prediction_strategy=multistep_prediction_strategy,
            multistep_prediction_win=multistep_prediction_win,
            multivariate_column_encoding=multivariate_column_encoding,
            store_lookback_history=store_lookback_history,
            **kwarg
        )

    def set_params(self, attr="steps", **params):
        super(LocalizedFlattenAutoEnsembler, self).set_params(**params)

    def name(self):
        return "LocalizedFlattenAutoEnsembler"
