from nose.tools import *
from datetime import datetime
import numpy as np
from longmantide import longmantide
import pandas as pd


def test_basic():
    lat = 40.7914  # Station Latitude
    lon = 282.1414  # Station Longitude
    alt = 370.  # Station Altitude [meters]
    model = longmantide.TideModel()  # Make a model object
    time = datetime(2015, 4, 23, 0, 0, 0)  # When we want the tide
    gm, gs, g = model.solve_longman(lat, lon, alt, time)
    np.testing.assert_almost_equal(gm, 0.0324029651226, 8)
    np.testing.assert_almost_equal(gs, -0.0288682178454, 8)
    np.testing.assert_almost_equal(g, 0.00353474727722, 8)

def test_series():
    lat = pd.Series(data=np.full(5, 40.7914))
    lon = pd.Series(data=np.full(5, 282.1414))
    alt = pd.Series(data=np.full(5, 370.))
    model = longmantide.TideModel()
    time = pd.DatetimeIndex(data=[datetime(2015, 4, 23, 0, 0, 0)]*5)
    gm, gs, g = model.solve_longman(lat, lon, alt, time)
    gm_expect = np.full(5, 0.0324029651226)
    gs_expect = np.full(-0.0288682178454)
    g_expect = np.full(0.00353474727722)
    np.testing.assert_array_almost_equal(gm, gm_expect, 8)
    np.testing.assert_array_almost_equal(gs, gs_expect, 8)
    np.testing.assert_array_almost_equal(g, g_expect, 8)
