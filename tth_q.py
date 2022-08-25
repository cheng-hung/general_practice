#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:19:19 2022

@author: chenghunglin
"""

import numpy as np

def tth_to_q(tth, wavelength):
    q = (4*np.pi/wavelength)*np.sin(tth*np.pi/360)
    return q


def q_to_tth(q, wavelength):
    tth = 2*180*np.arcsin(q*wavelength/(4*np.pi))/np.pi
    return tth

