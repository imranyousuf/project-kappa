from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
def plot_act(betaVols, meanData,mask,condition):
        
    meanData[~mask]=np.nan 
    betaVols[~mask]=np.nan
    nice_cmap_values = np.loadtxt('actc.txt')
    nice_cmap = colors.ListedColormap(nice_cmap_values,'actc')

    for i in range(meanData.shape[-1]):
        plt.imshow(meanData[:,:,i],cmap='gray',alpha=0.5,interpolation='nearest')
        plt.imshow(betaVols[:,:,i,condition-1],cmap=nice_cmap, alpha=0.5, interpolation ='nearest')
        plt.savefig('activation'+str(i)+'_'+str(condition-1)+'.png')
        plt.close()


