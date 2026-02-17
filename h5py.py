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




def print_time_fn(fn_list: list, time_limit:list = [None, None]):

    for fn in fn_list:
        try:
            f5 = h5py.File(fn, 'r')
            key = 'entry/instrument/detector/count_time'
            exp_t = np.asarray(f5[key])

            if time_limit[0]==time_limit[1]==None:
                print(f'{exp_t = }; {fn = }')

            elif (exp_t>=time_limit[0]) and (exp_t<=time_limit[1]):
                print(f'{exp_t = }; {fn = }')

        except (OSError, KeyError):
            pass
