from dipy.segment.mask import median_otsu
from scipy.ndimage import gaussian_filter
from loading_data import *

def smooth_mask(subject, run):
         """ Applies smoothing and computes mask. Applies mask to smoothed data """

         data = bold_data(subject, run)
         mean_data = np.mean(data,axis=-1)
         masked, mask = median_otsu(mean_data,2,1)
         smooth_data = gaussian_filter(data,[2,2,2,0])
         smooth_masked = smooth_data[mask]
         return smooth_masked.T


def masked_data(subject, run):
         data = bold_data(subject, run)
         mean_data = np.mean(data,axis=-1)
         masked, mask = median_otsu(mean_data,2,1)
         masked_data = data[mask]
         return masked_data.T

def smooth_data(subject, run):
         data = bold_data(subject, run)
         smooth_data = gaussian_filter(data,[2,2,2,0])
         return smooth_data
