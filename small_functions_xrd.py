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


'''
Calculate GoF for refinement
Formula source
https://en.wikipedia.org/wiki/Goodness_of_fit
https://github.com/scipy/scipy/issues/14298
https://math.stackexchange.com/questions/772391/normalization-for-chi-square-test
'''
def chi2_gof(y_obs, y_calc):
    
    y_obs = np.asarray(y_obs)
    y_calc = np.asarray(y_calc)
    
    y0 = y_obs/len(y_obs)
    y1 = y_calc/len(y_calc)

    chi2 = ((y0 - y1)**2/y1).sum()
    
    return chi2, np.sqrt(chi2)
    

    
    

    
'''
Calculate [r07], [r08] of IRF parameters for DEBUSSY
[r07]: the axial divergence width parameter
[r08]: the capillary width parameter
Formula source: DEBUSSY Section 2.3, P. 9-11
https://github.com/DeByeUSerSYstem/DEBUSSY_v2.2-UNIX/blob/main/macOSX/DEBUSSY_v2.2/MANUALS/Debussy_v2.2_Manual.pdf

s: the horizontal slit width / capillary length [mm]
h: the horizontal detector width / receiving slits length [mm]
R: the sample-detector distance [mm]
d: the capillary diameter [mm]
'''    
def axial_divergence(s, h, R):
    import numpy as np
    return (180/np.pi)*(s**2+h**2)/(24*R**2)



def capillary_width(d, R):
    import numpy as np
    return (180/np.pi)*(d)/(2*R)