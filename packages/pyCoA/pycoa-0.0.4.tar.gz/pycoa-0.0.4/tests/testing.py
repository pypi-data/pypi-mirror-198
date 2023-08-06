#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:27:17 2023

@author: Ioannis Nicolis
"""

import numpy as np
from numpy.testing import assert_allclose
import os
import sys
sys.path.append(os.path.join(os.getcwd(),"../src"))
from pyCoA import CoA

def test_CA():
    values = [68, 119,  26,   7,  20,  84,  17,  94,  15,  54,  14,  10,   5,  29,  14, 16]
    df = np.array(values).reshape((4,4)).transpose()
    x = CoA.CA(df)
    expected_eigenvalues = np.array([0.208772652, 0.022226615, 0.002598439])
    assert_allclose(x.eig, expected_eigenvalues)
    expected_rowcoord = np.array([-0.50456243, -0.14825270, -0.12952326, 0.83534777, -0.21482046, 0.03266635, 0.31964240, -0.06957934, 0.05550909, -0.04880414, 0.08315117, 0.01621471]).reshape((3,4)).transpose()
    assert_allclose(x.rowCoords, expected_rowcoord,rtol=1e-6)
    expected_colcoord = np.array([-0.492157672, 0.547413887, -0.212596927, 0.161753384, -0.088321513, -0.082954282, 0.167391087, 0.339039570, 0.021611305, -0.004709408, -0.100518284, 0.087597437]).reshape((3,4)).transpose()
    assert_allclose(x.columnCoords, expected_colcoord,rtol=1e-6)
