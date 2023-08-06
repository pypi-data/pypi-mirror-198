﻿"""
main entry-point for creation of :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
"""
#  /************** Begin Copyright - Do not add comments here **************
#   * Licensed Materials - Property of IBM
#   *
#   *   OCO Source Materials
#   *
#   *   (C) Copyright IBM Corp. 2020, All Rights Reserved
#   *
#   * The source code for this program is not published or other-
#   * wise divested of its trade secrets, irrespective of what has
#   * been deposited with the U.S. Copyright Office.
#   ***************************** End Copyright ****************************/
import numpy
import pandas as pd
import logging
from autoai_ts_libs.deps.tspy import _get_context
from autoai_ts_libs.deps.tspy.data_structures import MultiTimeSeries
import datetime

log = logging.getLogger(__name__)


def _numpy_array(tsc, data, granularity=None, start_time=None):
    """create a multi-time-series from a multi-dimensional numpy array

    Parameters
    ----------
    data : numpy.ndarray
    granularity : datetime.timedelta, optional
        the granularity for use in time-series :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.TRS.TRS` (default is None if no start_time, otherwise 1ms)
    start_time : datetime, optional
        the starting date-time of the time-series (default is None if no granularity, otherwise 1970-01-01 UTC)

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Examples
    --------

    create a multi-time-series from a numpy array

    >>> values = np.array([[1,2,3], [4,5,6], [7,8,9]])
    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(values)
    >>> mts
    0 time series
    ------------------------------
    TimeStamp: 0     Value: 1
    TimeStamp: 1     Value: 2
    TimeStamp: 2     Value: 3
    1 time series
    ------------------------------
    TimeStamp: 0     Value: 4
    TimeStamp: 1     Value: 5
    TimeStamp: 2     Value: 6
    2 time series
    ------------------------------
    TimeStamp: 0     Value: 7
    TimeStamp: 1     Value: 8
    TimeStamp: 2     Value: 9
    """
    return tsc.java_bridge.converters.from_numpy_to_mts(data, granularity, start_time)


def _from_observations(tsc, list_key_observation_pairs):
    """
    create a multi-time-series from a list of tuples (key, observation)

    Parameters
    ----------
    list_key_observation_pairs : list
        list of (key, observations) tuples

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Notes
    -----
    each time-series will be created from a group by operation on the key.

    Examples
    --------
    create a list of (key, observation) tuples

    >>> observations = [("a", autoai_ts_libs.deps.tspy.observation(2,1)), ("b", autoai_ts_libs.deps.tspy.observation(1,8)), ("a", autoai_ts_libs.deps.tspy.observation(1,7)), ("b", autoai_ts_libs.deps.tspy.observation(4,6)), ("c", autoai_ts_libs.deps.tspy.observation(1,5))]
    >>> observations
    [('a', TimeStamp: 2     Value: 1), ('b', TimeStamp: 1     Value: 8), ('a', TimeStamp: 1     Value: 7), ('b', TimeStamp: 4     Value: 6), ('c', TimeStamp: 1     Value: 5)]

    create a multi-time-series from observations

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(observations)
    >>> mts
    a time series
    ------------------------------
    TimeStamp: 1     Value: 7
    TimeStamp: 2     Value: 1
    b time series
    ------------------------------
    TimeStamp: 1     Value: 8
    TimeStamp: 4     Value: 6
    c time series
    ------------------------------
    TimeStamp: 1     Value: 5
    """
    return MultiTimeSeries(
        tsc,
        tsc.packages.time_series.core.timeseries.MultiTimeSeries.fromObservations(
            tsc.java_bridge.convert_to_java_list(
                tsc,
                list(
                    map(
                        lambda tup: tsc.packages.time_series.core.utils.Pair(
                            tup[0], tup[1]._j_observation
                        ),
                        list_key_observation_pairs,
                    )
                ),
            )
        ),
    )


def _df_instants(
    tsc, df, key_columns=None, ts_column=None, granularity=None, start_time=None
):
    """
    create a multi-time-series from a pandas dataframe in instants format. Instants format is defined as each
    time-series key being a separate column of the dataframe.

    Parameters
    ----------
    df : pandas dataframe
        the dataframe to convert to a multi-time-series
    key_columns : list, optional
        columns to use in multi-time-series creation (default is all columns)
    ts_column : string, optional
        column name containing time-ticks (default is time-tick based on index into dataframe)
    granularity : datetime.timedelta, optional
        the granularity for use in time-series :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.TRS.TRS` (default is None if no start_time, otherwise 1ms)
    start_time : datetime, optional
        the starting date-time of the time-series (default is None if no granularity, otherwise 1970-01-01 UTC)

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Examples
    --------
    create a simple df with a single index

    >>> import numpy as np
    >>> import pandas as pd
    >>> data = np.array([['', 'letters', 'timestamp', "numbers"],
                 ...['', "a", 1, 27],
                 ...['', "b", 3, 4],
                 ...['', "a", 5, 17],
                 ...['', "a", 3, 7],
                 ...['', "b", 2, 45]
                ...])
    >>> df = pd.DataFrame(data=data[1:, 1:],
                  ...columns=data[0, 1:]).astype(dtype={'letters': 'object', 'timestamp': 'int64', 'numbers': 'float64'})
      letters  timestamp  numbers
    0       a          1     27.0
    1       b          3      4.0
    2       a          5     17.0
    3       a          3      7.0
    4       b          2     45.0

    create a multi-time-series from a df using instants format

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series.df_instants(df, ts_column='timestamp')
    >>> mts
    numbers time series
    ------------------------------
    TimeStamp: 1     Value: 27.0
    TimeStamp: 2     Value: 45.0
    TimeStamp: 3     Value: 4.0
    TimeStamp: 3     Value: 7.0
    TimeStamp: 5     Value: 17.0
    letters time series
    ------------------------------
    TimeStamp: 1     Value: a
    TimeStamp: 2     Value: b
    TimeStamp: 3     Value: b
    TimeStamp: 3     Value: a
    TimeStamp: 5     Value: a
    """
    return tsc.java_bridge.converters.from_df_instants_to_mts(
        df, key_columns, ts_column, granularity, start_time
    )


def _df_observations(
    tsc,
    df,
    key_column,
    ts_column=None,
    value_column=None,
    granularity=None,
    start_time=None,
):
    """
    create a multi-time-series from a pandas dataframe in observations format. Observations format is defined as each
    record in the dataframe having a key, where each time-series is created by grouping unique keys.

    Parameters
    ----------
    df : pandas dataframe
        the dataframe to convert to a multi-time-series
    key_column : string
        column name containing the key
    ts_column : string, optional
        column name containing time-ticks (default is time-tick based on index into dataframe)
    value_column : list or string, optional
        column name(s) containing values (default is all columns)
    granularity : datetime.timedelta, optional
        the granularity for use in time-series :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.TRS.TRS` (default is None if no start_time, otherwise 1ms)
    start_time : datetime, optional
        the starting date-time of the time-series (default is None if no granularity, otherwise 1970-01-01 UTC)

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Examples
    --------
    create a simple df with a single index

    >>> import numpy as np
    >>> import pandas as pd
    >>> data = np.array([['', 'letters', 'timestamp', "numbers"],
                 ...['', "a", 1, 27],
                 ...['', "b", 3, 4],
                 ...['', "a", 5, 17],
                 ...['', "a", 3, 7],
                 ...['', "b", 2, 45]
                ...])
    >>> df = pd.DataFrame(data=data[1:, 1:],
                  ...columns=data[0, 1:]).astype(dtype={'letters': 'object', 'timestamp': 'int64', 'numbers': 'float64'})
      letters  timestamp  numbers
    0       a          1     27.0
    1       b          3      4.0
    2       a          5     17.0
    3       a          3      7.0
    4       b          2     45.0

    create a multi-time-series from a df using observations format where the key is letters

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series.df_observations(df, key_column="letters", ts_column='timestamp')
    a time series
    ------------------------------
    TimeStamp: 1     Value: {numbers=27.0}
    TimeStamp: 3     Value: {numbers=7.0}
    TimeStamp: 5     Value: {numbers=17.0}
    b time series
    ------------------------------
    TimeStamp: 2     Value: {numbers=45.0}
    TimeStamp: 3     Value: {numbers=4.0}
    """
    return tsc.java_bridge.converters.from_df_observations_to_mts(
        df, key_column, ts_column, value_column, granularity, start_time
    )


def _dict(tsc, ts_dict, granularity=None, start_time=None):
    """
    create a time-series from a dict where the values are either collections of observations or time-series

    Parameters
    ----------
    ts_dict : dict
        dict where one key per :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.ObservationCollection.ObservationCollection` or :class:`~autoai_ts_libs.deps.tspy.data_structures.time_series.TimeSeries.TimeSeries`
    granularity : datetime.timedelta, optional
        the granularity for use in time-series :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.TRS.TRS` (default is None if no start_time, otherwise 1ms)
    start_time : datetime, optional
        the starting date-time of the time-series (default is None if no granularity, otherwise 1970-01-01 UTC)

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Examples
    --------
    create a dict with observation-collection values

    >>> import autoai_ts_libs.deps.tspy
    >>> my_dict = {"ts1": autoai_ts_libs.deps.tspy.time_series([1,2,3]).materialize(), "ts2": autoai_ts_libs.deps.tspy.time_series([4,5,6]).materialize()}
    >>> my_dict
    {'ts1': [(0,1),(1,2),(2,3)], 'ts2': [(0,4),(1,5),(2,6)]}

    create a multi-time-series from dict without a time-reference-system

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series.dict(my_dict)
    >>> mts
    ts2 time series
    ------------------------------
    TimeStamp: 0     Value: 4
    TimeStamp: 1     Value: 5
    TimeStamp: 2     Value: 6
    ts1 time series
    ------------------------------
    TimeStamp: 0     Value: 1
    TimeStamp: 1     Value: 2
    TimeStamp: 2     Value: 3

    create a multi-time-series from dict containing a time-reference-system

    >>> import datetime
    >>> start_time = datetime.datetime(1990,7,6)
    >>> granularity = datetime.timedelta(days=1)
    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series.dict(my_dict, start_time=start_time, granularity=granularity)
    >>> mts
    ts2 time series
    ------------------------------
    TimeStamp: 1990-07-06T00:00Z     Value: 4
    TimeStamp: 1990-07-07T00:00Z     Value: 5
    TimeStamp: 1990-07-08T00:00Z     Value: 6
    ts1 time series
    ------------------------------
    TimeStamp: 1990-07-06T00:00Z     Value: 1
    TimeStamp: 1990-07-07T00:00Z     Value: 2
    TimeStamp: 1990-07-08T00:00Z     Value: 3
    """
    if granularity is None and start_time is None:
        trs = None
        j_trs = None
    else:
        if granularity is None:
            granularity = datetime.timedelta(milliseconds=1)
        if start_time is None:
            start_time = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
        from autoai_ts_libs.deps.tspy.data_structures.observations.TRS import TRS

        trs = TRS(tsc, granularity, start_time)
        j_trs = trs._j_trs

    j_ts_map = tsc.packages.java.util.HashMap()
    for k, v in ts_dict.items():
        try:
            if trs is None:
                j_ts_map.put(k, v._j_ts)
            else:
                # if time-series does not have a trs associated with it, we need to re-create
                if v.trs is None:
                    j_ts_map.put(k, v.materialize().to_time_series(start_time=trs.start_time, granularity=trs.granularity)._j_ts)
                else:
                    j_ts_map.put(k, v._j_ts)
        except:
            if trs is None:
                j_ts_map.put(k, v.to_time_series()._j_ts)
            else:
                j_ts_map.put(
                    k,
                    v.to_time_series(
                        start_time=trs.start_time, granularity=trs.granularity
                    )._j_ts,
                )

    return MultiTimeSeries(
        tsc, tsc.packages.time_series.core.timeseries.MultiTimeSeries(j_ts_map)
    )


def multi_time_series(*args, **kwargs):
    """creates a multi-time-series object

    Parameters
    ----------
    data:
        type `dict` or `pandas.DataFrame`, or :class:`numpy.ndarray`, or :class:`~autoai_ts_libs.deps.tspy.data_structures.io.TimeSeriesReader.TimeSeriesReader` or :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.ObservationCollection.ObservationCollection`

        * dict where one key per :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.ObservationCollection.ObservationCollection` or :class:`~autoai_ts_libs.deps.tspy.data_structures.time_series.TimeSeries.TimeSeries`

        * dataframe: there are two way to convert to MTS, depending upon the use-cases,
        (1) group by values of a given column [e.g. temperature time series and a bunch of locations (keys)],
        (2) each column is turned into its own time-series [a single timestamp and multiple metrics, e.g. temperature and humidity columns]

    key_column : string
        (only use when `data` is a pandas's DataFrame and use-case (1))
        column name containing the key, each key value is used for grouping data into a single-time-series. IMPORTANT: `key_column` and `key_columns` are used exclusively.

    key_columns : list, optional
        (only use when `data` is a pandas's DataFrame and use-case (2))
        columns to use in multi-time-series creation (default is all columns), i.e. each column is turned into its own time-series component.
        IMPORTANT: `key_column` and `key_columns` are used exclusively.

    ts_column : string, optional
        (only use when `data` is a pandas's DataFrame)
        column name containing time-ticks (default: time-tick is based on index into dataframe)

    value_column : list or string, optional
        (only use when `data` is a pandas's DataFrame and use-case (1))
        column name(s) containing values (default is all columns)

    granularity : datetime.timedelta, optional
        the granularity for use in time-series :class:`~autoai_ts_libs.deps.tspy.data_structures.observations.TRS.TRS` (default is None if no start_time, otherwise 1ms)

    start_time : datetime, optional
        the starting date-time of the time-series (default is None if no granularity, otherwise 1970-01-01 UTC)

    Returns
    -------
    :class:`~autoai_ts_libs.deps.tspy.data_structures.multi_time_series.MultiTimeSeries.MultiTimeSeries`
        a new multi-time-series

    Raises
    --------
    ValueError
        If there is an error in the input arguments, e.g. not a supporting data type

    Examples
    --------

    create a dict with observation-collection values

    >>> import autoai_ts_libs.deps.tspy
    >>> my_dict = {"ts1": autoai_ts_libs.deps.tspy.time_series([1,2,3]).materialize(), "ts2": autoai_ts_libs.deps.tspy.time_series([4,5,6]).materialize()}
    >>> my_dict
    {'ts1': [(0,1),(1,2),(2,3)], 'ts2': [(0,4),(1,5),(2,6)]}

    create a multi-time-series from dict without a time-reference-system

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(my_dict)
    >>> mts
    ts2 time series
    ------------------------------
    TimeStamp: 0     Value: 4
    TimeStamp: 1     Value: 5
    TimeStamp: 2     Value: 6
    ts1 time series
    ------------------------------
    TimeStamp: 0     Value: 1
    TimeStamp: 1     Value: 2
    TimeStamp: 2     Value: 3

    create a multi-time-series from a numpy array

    >>> values = np.array([[1,2,3], [4,5,6], [7,8,9]])
    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(values)
    >>> mts
    0 time series
    ------------------------------
    TimeStamp: 0     Value: 1
    TimeStamp: 1     Value: 2
    TimeStamp: 2     Value: 3
    1 time series
    ------------------------------
    TimeStamp: 0     Value: 4
    TimeStamp: 1     Value: 5
    TimeStamp: 2     Value: 6
    2 time series
    ------------------------------
    TimeStamp: 0     Value: 7
    TimeStamp: 1     Value: 8
    TimeStamp: 2     Value: 9

    * create a simple df with a single index

    >>> import numpy as np
    >>> import pandas as pd
    >>> data = np.array([['', 'letters', 'timestamp', "numbers"],
                 ...['', "a", 1, 27],
                 ...['', "b", 3, 4],
                 ...['', "a", 5, 17],
                 ...['', "a", 3, 7],
                 ...['', "b", 2, 45]
                ...])
    >>> df = pd.DataFrame(data=data[1:, 1:],
                  ...columns=data[0, 1:]).astype(dtype={'letters': 'object', 'timestamp': 'int64', 'numbers': 'float64'})
      letters  timestamp  numbers
    0       a          1     27.0
    1       b          3      4.0
    2       a          5     17.0
    3       a          3      7.0
    4       b          2     45.0

    create a multi-time-series from a df using instants format

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(df, ts_column='timestamp')
    >>> mts
    numbers time series
    ------------------------------
    TimeStamp: 1     Value: 27.0
    TimeStamp: 2     Value: 45.0
    TimeStamp: 3     Value: 4.0
    TimeStamp: 3     Value: 7.0
    TimeStamp: 5     Value: 17.0
    letters time series
    ------------------------------
    TimeStamp: 1     Value: a
    TimeStamp: 2     Value: b
    TimeStamp: 3     Value: b
    TimeStamp: 3     Value: a
    TimeStamp: 5     Value: a

    * create a simple df with a single index

    >>> import numpy as np
    >>> import pandas as pd
    >>> data = np.array([['', 'letters', 'timestamp', "numbers"],
                 ...['', "a", 1, 27],
                 ...['', "b", 3, 4],
                 ...['', "a", 5, 17],
                 ...['', "a", 3, 7],
                 ...['', "b", 2, 45]
                ...])
    >>> df = pd.DataFrame(data=data[1:, 1:],
                  ...columns=data[0, 1:]).astype(dtype={'letters': 'object', 'timestamp': 'int64', 'numbers': 'float64'})
      letters  timestamp  numbers
    0       a          1     27.0
    1       b          3      4.0
    2       a          5     17.0
    3       a          3      7.0
    4       b          2     45.0

    create a multi-time-series from a df using observations format where the key is letters

    >>> mts = autoai_ts_libs.deps.tspy.multi_time_series(df, key_column="letters", ts_column='timestamp')
    a time series
    ------------------------------
    TimeStamp: 1     Value: {numbers=27.0}
    TimeStamp: 3     Value: {numbers=7.0}
    TimeStamp: 5     Value: {numbers=17.0}
    b time series
    ------------------------------
    TimeStamp: 2     Value: {numbers=45.0}
    TimeStamp: 3     Value: {numbers=4.0}
    """
    tsc = _get_context()
    data = args[0]
    # key_column = args[1]
    if isinstance(data, pd.DataFrame):
        if len(args) == 2 or "key_column" in kwargs:
            return _df_observations(tsc, *args, **kwargs)
        elif len(args) == 1:
            return _df_instants(tsc, *args, **kwargs)
        else:
            msg = "Argument errors: invalid arguments"
            log.error(msg)
            raise ValueError(msg)

    elif isinstance(data, numpy.ndarray):
        return _numpy_array(tsc, data, **kwargs)
    elif isinstance(data, dict):
        return _dict(tsc, *args, **kwargs)
    elif isinstance(data, list):
        return _from_observations(tsc, *args, **kwargs)
    else:
        msg = "Argument error: invalid arguments"
        raise ValueError(msg)
