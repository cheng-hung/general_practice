import h5py
import numpy as np


# List all dataset keys, including subgroups

def get_dataset_keys(f):
    keys = []
    f.visit(lambda key : keys.append(key) if isinstance(f[key], h5py.Dataset) else None)
    return keys


f = 'xxxxx.h5'
f_h5 = h5py.File(f, 'r')

get_dataset_keys(f_h5)
