import numpy as np

def diff_corr(betas, condition):
    differences = []
    betas_2d = betas.reshape((-1,betas.shape[-1]))
    betas_2d_T = betas_2d.T    

    for i in np.arange(8)[np.arange(8)!=condition-1]:
        differences.append(betas_2d_T[i,:] - betas_2d_T[condition-1,:])

    return np.corrcoef(differences)
