import nibabel as nib
import numpy as np
import os

def merge_bold(subject):
	sub_path = os.path.realpath(subject)
	runs_path = ['BOLD/task001_run'+ i + '/bold.nii.gz' for i in ['001','002','003','004','005','006','007','008','009','010','011’,’012’]]
	bolds_list = [nib.load(os.path.join(sub_path, runs_path[i])).get_data() for i in range(len(runs_path))]
	merged = np.concatenate(bolds_list, axis = 3)
	return merged

def merge_bold_5(subject):
	sub_path = os.path.realpath(subject)
	runs_path = ['BOLD/task001_run'+ i + '/bold.nii.gz' for i in ['001','002','003','004','005','006','007','008','009','010','011']]
	bolds_list = [nib.load(os.path.join(sub_path, runs_path[i])).get_data() for i in range(len(runs_path))]
	merged = np.concatenate(bolds_list, axis = 3)
	return merged
