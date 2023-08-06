################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2021, 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

import unittest
import logging
import numpy as np
import glob
import os
from autoai_ts_libs.utils.score import Score
import pandas as pd
import sys

# logger = logging.getLogger()


# saved models were created by running:
# python3 run_time_series_daub.py -df time_series_fvt/repository/input/data/Air_Quality.csv -tc 1 2 -tsc 0 -imp true -impth 0.3 -impl Linear -ph 2 -mnde 10 -of ~/Documents/IBM/Research/IOT/autoai_ts_libs/tests/notebook_support/models/test -ompath ~/Documents/IBM/Research/IOT/autoai_ts_libs/tests/notebook_support/models -rrtc True

data_path = "data/Air_Quality.csv"

class FitTest(unittest.TestCase):
    def setUp(self):        
        file_path = os.path.realpath(__file__)
        cwdir = os.path.split(file_path)[0]
        if (sys.version_info >= (3, 8)) and (sys.version_info < (3, 9)):
            print("Python version: 3.8")
            models_location = "models/python38"
        elif sys.version_info >= (3, 9) and (sys.version_info < (3, 10)):
            print("Python version: 3.9")
            models_location = "models/python39"
        elif sys.version_info >= (3, 10) and (sys.version_info < (3, 11)):
            print("Python version: 3.10")
            models_location = "models/python310"
        self.saved_model_path = os.path.join(cwdir, models_location)
        self.num_models = 10
        # print("saved_model_path", self.saved_model_path)
        # create a perturbed subsample which is larger
        X = pd.read_csv(os.path.join(cwdir, "..", "data", "Air_Quality.csv"))
        columns = [1, 2]
        l = min(200, X.shape[0])
        self.Xp = X.iloc[-l:,columns] + np.sqrt(0.1)*np.random.randn(l, len(columns)) + 10

    def tearDown(self):
        pass

    def test_load_and_fit(self):

        Xp = self.Xp
        models = glob.glob(os.path.join(self.saved_model_path, "*.pkl"))
        # first ensure we have the right count of models
        self.assertEqual(len(models),self.num_models)

        for p in models:
            with self.subTest(model_path=p, test="Load model"):
                print(p)
                m = Score.load(p)
            with self.subTest(model_path=p, test="predict(None)"):
                z = m.predict(None)
            with self.subTest(model_path=p, test="fit()"):
                m.fit(Xp, Xp)
                z2 = m.predict(None)
                # this test was too aggressive
                # self.assertGreater(np.mean(z2-z),0)
                self.assertEqual(z2.shape, z.shape)


if __name__ == "__main__":
    unittest.main()