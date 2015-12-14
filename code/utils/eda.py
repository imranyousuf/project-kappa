""" Script to run eda


"""
from convolve import *
from events2neural_fixed import *
from harmonic import *
from loading_data import *
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
import nibabel as nib
from dipy.segment.mask import median_otsu
from design_matrix import *


#I. Subject and Run

############## 
subject = 'sub001'
run = 1
############## 

#Loading Data and HDR
data = bold_data(subject, 1)
vol_shape, n_trs = data.shape[:-1], data.shape[-1]

TR = 2.5
tr_times = np.arange(0,30,TR)
all_tr_times = np.arange(n_trs) * TR
hrf_at_trs = hrf(tr_times)

X = np.ones((n_trs,14))
X_np = np.ones((n_trs,14))

mean_data = np.mean(data,axis=-1)
masked, mask = median_otsu(mean_data,2,1)

Y = data[mask].T
col = 0
pred = 0

#Adding onsets to design matrix
for i in list_cond_file(subject,run):
    neural_prediction = events2neural_fixed(i, TR, n_trs)
    convolved = convolve(neural_prediction, hrf_at_trs)
    X[:,col] = convolved
    X_np[:,pred] = neural_prediction
    col = col + 1
    pred = pred + 1

plt.plot(all_tr_times ,X_np[:,:8])
plt.savefig('block.png')
plt.close()

plt.plot(all_tr_times ,X_np[:,:8])
plt.plot(all_tr_times, X[:,:8])
plt.savefig('block_and_hdr.png')
plt.close()

#II. Design

#Masking Thresholds

#Run 1
data = bold_data(subject, 1)
mean_vol = np.mean(data, axis=-1)

plt.hist(np.ravel(mean_vol), bins=100)
plt.savefig('sub1_run1_mask.png')
plt.close()

#mean_data = np.mean(data,axis=-1)
#masked, mask = median_otsu(mean_data,2,1)


#Run 3
data3 = bold_data(subject, 3)
mean_vol2 = np.mean(data3, axis=-1)

plt.hist(np.ravel(mean_vol2), bins=100)
plt.savefig('sub1_run3_mask.png')
plt.close()

#mean_data2 = np.mean(data3,axis=-1)
#masked, mask2 = median_otsu(mean_data2,2,1)


#Run 5
data5 = bold_data(subject, 5)
mean_vol3 = np.mean(data5, axis=-1)

plt.hist(np.ravel(mean_vol3), bins=100)
plt.savefig('sub1_run5_mask.png')
plt.close()

#mean_data3 = np.mean(data5,axis=-1)
#masked, mask3 = median_otsu(mean_data3,2,1)


#Applied Mask to mean_data
mean_data[~mask]=np.nan 
plt.imshow(mean_data[:,:,45],cmap='gray',alpha=0.5,interpolation='nearest')

#mean_data2[~mask2]=np.nan
#plt.imshow(mean_data2[:,:,45],cmap='gray',alpha=0.5,interpolation='nearest')

#mean_data3[~mask3]=np.nan
#plt.imshow(mean_data3[:,:,45],cmap='gray',alpha=0.5,interpolation='nearest')


#Design Matrix
plt.imshow(X[:,0:9], aspect = 0.1, interpolation = 'nearest', cmap = 'gray')
plt.colorbar()
plt.savefig('desing_matrix.png')
plt.close()

X, Y, betas_vols, mask, U, Y_demeaned, mean_data, projection_vols = design_matrix(subject, run)
plt.imshow(X, aspect = 0.1, interpolation = 'nearest', cmap = 'gray')
plt.colorbar()
plt.savefig('desing_matrix_dt_pca.png')
plt.close()

#Betas Values
betas_vols[~mask]=np.nan

plt.imshow(betas_vols[:,:,45,0], interpolation ='nearest')
plt.savefig('betas_vols_house.png')
plt.close()

plt.imshow(betas_vols[:,:,45,7], interpolation ='nearest')
plt.savefig('betas_vols_face.png')
plt.close()

plt.imshow(betas_vols[:,:,45,5], interpolation ='nearest')
plt.savefig('betas_vols_scissors.png')
plt.close()

#PCA
Y_demeaned = Y - np.mean(Y, axis=1).reshape([-1, 1])

Y_demeaned_2 = np.mean(Y_demeaned, axis = 0)
Y_demeaned_fix = Y_demeaned - Y_demeaned_2
u_cov = Y_demeaned_fix.dot(Y_demeaned_fix.T)
U, S, V = npl.svd(u_cov)

plt.plot(S)
plt.savefig('components_variance.png')

#PCA Projections
for i in range(10):
    plt.imshow(projection_vols[:,:,45,i], cmap = 'gray')
    plt.savefig('projection_' + str(i) + '.png')

# Some final checks that you wrote the files with their correct names
from os.path import exists
#assert exists('vol_std_values.txt')
#assert exists('vol_std_outliers.txt')
#assert exists('vol_std.png')
#assert exists('vol_rms_outliers.png')
#assert exists('extended_vol_rms_outliers.png')
#assert exists('extended_vol_rms_outliers.txt')
#assert exists('mean_mrss_vals.txt')

