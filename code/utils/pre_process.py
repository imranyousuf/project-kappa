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

def mask_data(subject, run):
       
         sub_path = os.path.realpath(subject)
         sub_path_bold= sub_path + '/BOLD'
         bold_path = [ i for i in os.listdir(sub_path_bold) if not (i.startswith('.'))]
         list_bold_path= [sub_path_bold + '/' + i for i in bold_path]
         fname  =  list_bold_path[run-1] + '/' + 'bold.nii' 
         means_img = mean_img(fname)
         masking_img = compute_epi_mask(fname)
         masked_data = apply_mask(fname,masking_img)
         return masked_data



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
