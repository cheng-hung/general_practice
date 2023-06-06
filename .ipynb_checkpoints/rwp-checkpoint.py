import numpy as np
# import pandas as pd

'''
Calculate Rwp for refinement
Formula source
http://pd.chem.ucl.ac.uk/pdnn/refine1/practice.htm
http://pd.chem.ucl.ac.uk/pdnn/refine1/rfacs.htm
'''


def rwp_delta(y_obs, y_calc, weight='count'):
    
    y_obs = np.asarray(y_obs)
    y_calc = np.asarray(y_calc)
    
    if weight == 'count':
        w = 1/y_obs
    delta = (w*(y_obs-y_calc)**2).sum()
    rwp_2 = delta/(w*(y_obs)**2).sum()
    
    return np.sqrt(rwp_2)*100, delta


