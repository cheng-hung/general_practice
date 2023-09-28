#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:21:48 2022

@author: chenghunglin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %matplotlib qt
plt.close('all')

fn_dir = '/Users/chenghunglin/Library/CloudStorage/OneDrive-BrookhavenNationalLaboratory/data_processing/20220311_DSE_test/pre_process/'
fn = 'CsPbBr3_20211114-120845_bkg_Dioptas_q.xy'

df = pd.read_csv(fn_dir+fn, sep='  ' ,names=['q', 'I'], skiprows=24 ,keep_default_na=True)

# f1, (ax1, ax2) = plt.subplots(1, 2, figsize = (6, 9), gridspec_kw={'width_ratios': [1,1]})
f1, ax1 = plt.subplots(1, 1, figsize = (12, 4))
ax1.plot(df.q, df.I)
ax1.set_xlim(0.8, 6)
plt.show()

imag_name = fn[:-3] + '_01.png'
plt.savefig(fn_dir+imag_name, dpi = 600,  transparent=True)