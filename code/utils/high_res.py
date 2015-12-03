import numpy as np
import nibabel as nib
import os
from list_cond import *
from path_bold import *
from cond_path import *

def highRes_data(subject, task_num, TR = 2.5, tr_divs = 10):
	""" This functions returs high resolution data

	Parameter
	---------
	subject: str
		Please specific the subject. For example, you should input 'sub001' if choose the first subject
	task_num: str
		Please specific the subject. For example, you should input 'task001_run001' if choose the first run.
	TR: float
		TR in seconds
	tr_divs: int
		number of the steps per TR

	Results
	-------
	X: 2D array
		This is high resolution bold data corresponding to each category(predictor variable)

	y: 1D array
		This is response variable corresponding to each category


	"""
	img = nib.load(path_bold(subject, task_num) + '/bold.nii.gz')
	data = img.get_data()
	n_trs = data.shape[-1]
	data_2d = np.reshape(data, (121,-1))
	high_res_data = np.repeat(data_2d, tr_divs, axis = 0) 


	high_res_times = np.arange(0, n_trs, 1 / tr_divs) * TR
	high_res_neural = np.zeros(high_res_times.shape)

	X = []

	num = 1
	
	condition = list_every_cond(subject, task_num)

	for i in condition:
		category = np.loadtxt(cond_path(subject, task_num, cond_num = i))
		high_category_res_onset  = category[:, :2] / TR * tr_divs

		for onset, duration in high_category_res_onset:
			high_res_neural[onset:onset + duration] = num

		for j, k in high_category_res_onset.astype(int):
			X.append(high_res_data[j:j+k])

		num = num + 1

	X = np.array(X)
	X = np.reshape(X, (X.shape[0] * X.shape[1], -1))
	y = np.sort(high_res_neural[np.nonzero(high_res_neural)])

	return X, y

	
