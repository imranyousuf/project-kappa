import numpy as np  
import matplotlib.pyplot as plt  
from stimuli import events2neural
from harmonic import *
from cond_path import *
from list_cond import *
from convolve import *
import numpy.linalg as npl
from matrix_image import *
from path_bold import *
import nibabel as nib

# Load the sub001 task001_run001 data
img = nib.load(path_bold('sub001', 'task001_run001')+ '/bold.nii.gz')
data = img.get_data()


# TR is 2,5 second
TR = 2.5
tr_times = np.arange(0, 30, TR)



# The number of the voxel is 121
n_vols = 121
all_tr_times = np.arange(121) * TR



for i in list_every_cond('sub001', 'task001_run001'):
	neural = events2neural(cond_path('sub001', 'task001_run001', i), TR, n_vols)
	convolved = convolve(neural, hrf(tr_times))
	plt.plot(all_tr_times, neural)
	plt.plot(all_tr_times, convolved)

plt.close()

# There are 8 categories, and 121 features each categories. 

X = np.ones((n_vols, 8 + 1))

#There are 8 categories, so the data matrix has 9 colomns. 
#The order of the column is house, scrambledpix, cat, shoe, bottle, scissors, chair, face. 
# Let the first column starts from index 0
col = 0

# create data matrix
for i in list_every_cond('sub001', 'task001_run001'):
	neural = events2neural(cond_path('sub001', 'task001_run001', i), TR, n_vols)
	convolved = convolve(neural, hrf(tr_times))
	X[:, col] = convolved
	col = col + 1

# Show the graph of the design matrix
show_design(X)
	
# We find the β for our data and design
time_by_vox = np.reshape(data, (-1, n_vols)).T
Xp = npl.pinv(X)
beta_hats = Xp.dot(time_by_vox)
