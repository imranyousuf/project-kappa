from matplotlib import colors
import numpy as np
import os
import matplotlib.pyplot as plt
def plot_act(subject, betas_vols, mean_data, mask, condition ):
        
    mean_data[~mask]=np.nan 
    betas_vols[~mask]=np.nan

    activation_path = str(subject) + '_c' + str(condition) + '_act'
    os.makedirs(activation_path)

    for i in range(mean_data.shape[-1]):
        plt.imshow(mean_data[:,:,i],cmap='gray',alpha=0.5,interpolation='nearest')
        plt.imshow(betas_vols[:,:,i,condition-1], alpha=0.5, interpolation ='nearest')
        plt.savefig(activation_path + '/activation'+str(i)+'_'+str(condition-1)+'.png')
        plt.close()


