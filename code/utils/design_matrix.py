import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
import nibabel as nib
from dipy.segment.mask import median_otsu
from scipy.ndimage import gaussian_filter
from matplotlib import colors
from scipy.misc import imread
from loading_data import *
from harmonic import *
from pre_process import *
from convolve import *
from events2neural_fixed import events2neural_fixed
import numpy.linalg as npl


def design_matrix(subject, run, TR = 2.5):

      data = bold_data(subject,run)
      vol_shape, n_trs = data.shape[:-1], data.shape[-1]
      tr_times = np.arange(0,30,TR)
      hrf_at_trs = hrf(tr_times)
      col = 0
      X = np.ones((n_trs,14))

      #Smoothed and masked data
      mean_data = np.mean(data,axis=-1)
      masked, mask = median_otsu(mean_data,2,1)
      # smooth_data = gaussian_filter(data,[2,2,2,0])
      # Y = smooth_data[mask].T
      #omitted smoothing for now
      Y = data[mask].T
      
      #Adding onsets to design matrix
      for i in list_cond_file(subject,run):
          neural_prediction = events2neural_fixed(i, TR, n_trs)
          convolved = convolve(neural_prediction, hrf_at_trs)
          X[:,col] = convolved
          col = col+1


      ##PCA
      Y_demeaned = Y - np.mean(Y,axis=1).reshape([-1,1])
      unscaled_cov = Y_demeaned.dot(Y_demeaned.T) 
      U, S, V = npl.svd(unscaled_cov)
      X[:,8] = U[:,0]
      X[:,9:11] = U[:,6:8] 

     


      linear_drift = np.linspace(-1,1,n_trs)
      X[:,11] = linear_drift
      quadratic_drift = linear_drift ** 2
      quadratic_drift -= np.mean(quadratic_drift)
      X[:,12]= quadratic_drift

      betas = npl.pinv(X).dot(Y)
      betas_vols = np.zeros(vol_shape+(14,))
      betas_vols[mask,:] = betas.T
      
      projections = U.T.dot(Y_demeaned)
      projection_vols = np.zeros(data.shape)
      projection_vols[mask,:] = projections.T
          
      return X, Y, betas_vols, mask, U, Y_demeaned, mean_data, projection_vols
