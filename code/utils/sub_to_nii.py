import nibabel as nib
import numpy as np
from get_affine import get_affine

def sub_to_nii(sub_fMRI_data, sub):
	new_img = nib.Nifti1Image(sub_fMRI_data, get_affine(sub))
	nib.save(new_img, sub + '.nii')

def sub_to_nii_5(sub_fMRI_data, sub):
	new_img = nib.Nifti1Image(sub_fMRI_data, get_affine_5(sub))
	nib.save(new_img, sub + '.nii')
