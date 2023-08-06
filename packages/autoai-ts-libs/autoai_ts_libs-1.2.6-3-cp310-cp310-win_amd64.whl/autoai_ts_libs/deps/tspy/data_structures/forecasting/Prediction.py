﻿class Prediction:
    """
    The basic unit for a value returned from forecasting

    Values can be of type float or list
    """
    def __init__(self, tsc, j_prediction):
        self._tsc = tsc
        self._j_prediction = j_prediction

    @property
    def value(self):
        """The value of the prediction
        Returns
        -------
        float or list
            the value of the prediction
        """
        v = self._tsc.java_bridge.cast_to_py_if_necessary(self._j_prediction.getValue())[0]
        if self._tsc.java_bridge.is_instance_of_java_class(v, "java.util.List"):
            v = [v.get(i) for i in range(v.size())]
        return v

    @property
    def lower_bound(self):
        """The lower bound of the confidence interval
        Returns
        -------
        float
            the lower bound of the confidence interval
        """
        return self._j_prediction.getLowerBound()

    @property
    def upper_bound(self):
        """The upper bound of the confidence interval
        Returns
        -------
        float
            the upper bound of the confidence interval
        """
        return self._j_prediction.getUpperBound()

    @property
    def error(self):
        """the error of the prediction
        Returns
        -------
        float
            the error of the prediction
        """
        return self._j_prediction.getError()

    def toString(self):
        return str(self._j_prediction.toString())
    def __str__(self):
        return str(self._j_prediction.toString())
