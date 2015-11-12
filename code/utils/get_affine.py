import numpy as np
import nibabel as nib
import os

def get_affine(subject):
	sub_path = os.path.realpath(subject)
	runs_path = ['BOLD/task001_run'+ i + '/bold.nii.gz' for i in ['001','002','003','004','005','006','007','008','009','010','011', '012']]
	affine_list = [nib.load(os.path.join(sub_path, runs_path[i])).affine for i in range(len(runs_path))]
	return affine_list[0]

def get_affine_5(subject):
        sub_path = os.path.realpath(subject)
        runs_path = ['BOLD/task001_run'+ i + '/bold.nii.gz' for i in ['001','002','003','004','005','006','007','008','009','010','011']]
        affine_list = [nib.load(os.path.join(sub_path, runs_path[i])).affine for i in range(len(runs_path))]
        return affine_list[0]

