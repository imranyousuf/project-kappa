import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os
from nilearn.masking import compute_epi_mask
from nilearn.image.image import mean_img
from nilearn.plotting.img_plotting import plot_epi, plot_roi
from nilearn.masking import apply_mask
from nilearn.masking import compute_epi_mask
from nilearn.image.image import mean_img
from nilearn.plotting.img_plotting import plot_epi, plot_roi


def compute_mask(subject, run):
       
         sub_path = os.path.realpath(subject)
         sub_path_bold= sub_path + '/BOLD'
         bold_path = [ i for i in os.listdir(sub_path_bold) ]
         list_bold_path= [sub_path_bold + '/' + i for i in bold_path]
         fname  =  list_bold_path[run-1] + '/' + 'bold.nii'
         means_img = mean_img(fname)
         masking_img = compute_epi_mask(fname)
         masked_data = apply_mask(fname,masking_img)
         return masked_data

def plot_masked_img(masked_data):
         plt.figure(figsize=(7, 5))
         plt.plot(masked_data[:2, :150].T)
         plt.xlabel('Time [TRs]', fontsize=16)
         plt.ylabel('Intensity', fontsize=16)
         plt.xlim(0, 150)
         plt.subplots_adjust(bottom=.12, top=.95, right=.95, left=.12)
         return plt.show()

