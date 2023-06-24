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



'''
Calculate global mean and standard deviation with probability
https://stackoverflow.com/questions/67545203/how-to-calculate-standard-deviation-in-python-when-x-and-px-are-known
https://www.rapidtables.com/calc/math/variance-calculator.html                           
https://stats.stackexchange.com/questions/210472/negative-variance-result-when-calculating-standard-deviation
'''
def mean_std_pro(x, pro):
    x = np.asarray(x)
    pro = np.asarray(pro)
            
    ex = x * pro
    # ex2 = x**2 * pro
    mean = ex.sum() / pro.sum()
    # variance = ex2.sum() - ex.sum()**2
    var = (x-mean)**2 * pro
    
    if round(pro.sum()) == 1:
        variance = var.sum()
    else:
        variance = var.sum()/(pro.sum()-1)
        
    std_dev = variance**0.5

    return mean, std_dev



'''
Calculate Biso to Uiso or vice versa
'''
def Biso_to_Uiso(b):
    return b/(8*np.pi**2)

def Uiso_to_Biso(u):
    return u*(8*np.pi**2)  

