# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:33:32 2017

@author: Katie
"""


#import pandas as pd # can't use with pypy
import os
import sys
import pickle
sys.path.append("..")

from clsInputs import clsInputs

inputs = pickle.load( open(os.path.join('C:\Users\Katie\Dropbox\MAST-1D_version_K15\Output\PreRemoval\EDamIndex3Mob05AlphaN07AlphaG055NewAvulsion_test', 'inputparams.inputs'), "rb" ) )
print inputs.ErodeT