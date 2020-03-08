import numpy as np
import numpy.testing as npt

import Giter

def test_Giter_smoke():
    #Smoke_test
    obt = Giter.Giter_object()

def test_Giter_object_fizz():
    #test the fizz_function
    obj = Giter.Giter_object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")
