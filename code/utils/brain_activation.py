import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
import nibabel as nib
from dipy.segment.mask import median_otsu
from scipy.ndimage import gaussian_filter
from matplotlib import colors
from scipy.misc import imread

def brain_activation(subject, task_run, condition, TR = 2.5):
	img = nib.load(path_bold(subject, task_run) + 'filtered_func_data_mni.nii.gz')
	data = img.get_data()

	vol_shape, n_trs = data.shape[:-1], data.shape[-1]
	col = 0
	X = np.ones((n_trs, 10))
	tr_times = np.arange(0, 30, TR)
	hrf_at_trs = hrf(tr_times)
	n_to_remove = len(hrf_at_trs) - 1

	for i in list_every_cond(subject, task_run):
		neural = events2neural(cond_path(subject, task_run, i), TR, n_trs)
		convolved = np.convolve(neural, hrf_at_trs)
		convolved = convolved[:-n_to_remove]
		X[:, col] = convolved
		col = col + 1

	mean_data = np.mean(data, axis=-1)
	masked, mask = median_otsu(mean_data, 2, 1)
	linear_drift = np.linspace(-1, 1, n_trs)
	X[:, 8] = linear_drift

#Masking and Modeling Noise
	in_brain_tcs = data[mask, :]
	Y = in_brain_tcs.T

	betas = npl.pinv(X).dot(Y)
	beta_vols = np.zeros(vol_shape + (10,))
	beta_vols[mask] = betas.T

#Showing Parameter Maps with Color
	smooth_data = gaussian_filter(data, [2, 2, 2, 0])
	Y = smooth_data[mask].T

	betas = npl.pinv(X).dot(Y)
	beta_vols = np.zeros(vol_shape + (10,))
	beta_vols[mask] = betas.T

	mean_data[~mask] = np.nan
	beta_vols[~mask] = np.nan

	nice_cmap_values = np.loadtxt('actc.txt')
	nice_cmap = colors.ListedColormap(nice_cmap_values, 'actc')

	for i in range(mean_data.shape[-1]):
		plt.imshow(mean_data[:, :, i], cmap='gray', alpha=0.5, interpolation = 'nearest')
		plt.imshow(beta_vols[:, :, i, condition], cmap=nice_cmap, alpha=0.5, interpolation = 'nearest')
		plt.savefig('activation' + str(i) + '.png')
		plt.close()