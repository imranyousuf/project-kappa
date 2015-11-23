import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os
import diagnostics as dg



#try to organize data based on subject ex sub001


def open_bold (subject):
	""" Find all task_run files from a subject BOLD """ 

	sub_path = os.path.realpath(subject)
	sub_path_BOLD = sub_path + '/BOLD'
	task_run = [ i for i in os.listdir(sub_path_BOLD) if not (i.startswith('.'))]

	return task_run

def path_bold(subject):
	""" Get the path of BOLD """

	sub_path = os.path.realpath(subject)
	return sub_path + '/BOLD'


def open_anatony(subject):
	""" Open highres001_brain """

	sub_path = os.path.realpath(subject)
	return sub_path + '/anatomy/highres001_brain.nii.gz'

## work on subject 1

#Extract Brain data
brain_directory = open_anatony('sub001')
brain_img = nib.load(brain_directory)
data = brain_img.get_data()

#Extract each task
sub001_task_run = open_bold('sub001')
sub001_task_run

#Get the BOLD path
sub001_path_BOLD = path_bold('sub001')

#Get the each data of each task run
run_img_result = {x: sub001_path_BOLD + "/" + x + '/bold.nii.gz' for x in sub001_task_run}

#Plot the standard deviation for each run
for i in run_img_result.keys():
	img = nib.load(run_img_result[i])
	data = img.get_data()
	vol_stds = dg.vol_std(data)
	outliers, thresholds = dg.iqr_outliers(vol_stds)
	N = len(vol_stds)
	x = np.arange(N)
	plt.plot(vol_stds, label='vol std')
	plt.plot(x[outliers], vol_stds[outliers], 'o', label='outliers')
	plt.plot([0, N], [thresholds[0], thresholds[0]], ':', label='IQR lo')
	plt.plot([0, N], [thresholds[1], thresholds[1]], ':', label='IQR hi')
	plt.xlabel('Voxel')
	plt.ylabel('Volume standard deviation')
	plt.title('Volume Standard Deviation_' + i)
	plt.legend(fontsize = 8)
	plt.savefig( i + '_vol_std.png')
	plt.close()

# plot the RMS difference values
for i in run_img_result.keys():
	img = nib.load(run_img_result[i])
	data = img.get_data()
	rms_dvals = dg.vol_rms_diff(data)
	rms_outliers, rms_thresholds = dg.iqr_outliers(rms_dvals)
	N = len(rms_dvals)
	x = np.arange(N)
	plt.plot(rms_dvals, label='vol RMS differences')
	plt.plot(x[rms_outliers], rms_dvals[rms_outliers], 'o', label='outliers')
	plt.plot([0, N], [rms_thresholds[0], rms_thresholds[0]], ':', label='IQR lo')
	plt.plot([0, N], [rms_thresholds[1], rms_thresholds[1]], ':', label='IQR hi')
	plt.xlabel('Voxel')
	plt.ylabel('Volumn RMS difference values')
	plt.title('Volume RMS difference values_' + i)
	plt.legend(fontsize = 8)
	plt.savefig( i + '_vol_rms_outliers.png')
	plt.close()















