import os
import pandas as pd

def get_rwo_header(fn, sep=' ', num_data_column=2, check_range=100, check_float=True):

    cont_01 = []
    with open(fn, 'r') as f:
        cont = f.readlines()
        f.close()
    
    for line in cont:
        new_line = line.strip('\n').split(sep)
        cont_01.append(new_line)

    i = 0
    while i < len(cont_01):
        c0 = (len(cont_01[i]) == num_data_column)
        c1 = all([len(l)==num_data_column for l in cont_01[i:i+check_range]])
        c2 = (is_float(cont_01[i][0]) and is_float(cont_01[i][1]))

        if check_float:
            if c0 and c1 and c2:
                # print(f'Num of rows of header is {i}.')
                break
        else:
            if c0 and c1:
                # print(f'Num of rows of header is {i}.')
                break
            
        i += 1

    return i



def is_float(s):    
    """
    Checks if a string can be successfully converted to a float.
    
    Args:
    s: The string to check.
    
    Returns:
    True if the string can be converted to a float, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

    
