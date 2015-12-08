from matplotlib import colors
import numpy as np  
import matplotlib.pyplot as plt  
from stimuli import events2neural
from linear_model import *
from cond_path import *
from list_cond import *
from convolve import *
import numpy.linalg as npl
from matrix_image import *
from path_bold import *
import nibabel as nib
from scipy.ndimage import gaussian_filter
from dipy.segment.mask import median_otsu



def brain_activation(subject, task_run, TR = 2.5):


	img = nib.load(path_bold(subject, task_run) + '/bold.nii.gz')
	data = img.get_data()
	vol_shape, n_trs = data.shape[:-1], data.shape[-1]
	tr_times = np.arange(0, 30, TR)
	col = 0
	X = np.ones((n_trs, 10))
	for i in list_every_cond(subject, task_run):
		neural = events2neural(cond_path(subject, task_run, i), TR, n_trs)
		convolved = convolve(neural, hrf(tr_times))
		X[:, col] = convolved
		col = col + 1

	X[:, 8] = np.linspace(-1, 1, n_trs)
	mean_data = data.mean(axis=-1)
	masked, mask = median_otsu(mean_data, 2, 1)
	smooth_data = gaussian_filter(data, [2, 2, 2, 0])
	Y = smooth_data[mask].T
	betas = npl.pinv(X).dot(Y)
	beta_vols = np.zeros(vol_shape + (10,))
	beta_vols[mask] = betas.T
	
	return beta_vols
	

a = brain_activation


mean_data[~mask] = np.nan
beta_vols[~mask] = np.nan
from matplotlib import colors
nice_cmap_values = np.loadtxt('actc.txt')
nice_cmap = colors.ListedColormap(nice_cmap_values, 'actc')
plt.imshow(mean_data[:, :, 31], cmap='gray', alpha=0.5)
plt.imshow(beta_vols[:, :, 31, 0], cmap=nice_cmap, alpha=0.5)
