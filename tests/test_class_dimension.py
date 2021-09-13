from source import Dimention
import numpy as np


def test_func_dim_10():
    assert Dimention.dim(range(10))[0] == 10


def test_func_dim_2d():
    assert Dimention.dim(np.ones([4, 6]))[0] == 4
    assert Dimention.dim(np.ones([4, 6]))[1] == 6
