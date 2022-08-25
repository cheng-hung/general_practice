#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:35:50 2022

@author: chenghunglin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

in_dir = '/Users/chenghunglin/Desktop/test/20220502_CsPbBr_tetra_SPH_30nm/DFA_clx/'
fn = 'CsPbBr3_20220502_tetra_SPH_RMbkg.csv'

data = pd.read_csv(in_dir+fn, names=['tth', 'I'], keep_default_na=True)
# pd.set_option('display.float_format', '{:.8e}'.format)
# data.tth.apply(lambda x: '{:.8e}'.format(x))
# data = data.astype(str)

# fn_out = 'CsPbBr3_20211114-120845_bin.xy'
fn_out = fn[:-4] + '.xy'
data.to_csv(in_dir+fn_out, sep=' ', index=False, header=False, float_format='{:.8e}'.format)


