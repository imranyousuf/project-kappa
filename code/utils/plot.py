import numpy as np
import nibabel as nib 
import matplotlib.pyplot as plt
import diagnostics as dig
import numpy.linalg as npl

def plot_vol_std_values(vol_std_values):
	plt.plot(np.arange(len(vol_std_values)), vol_std_values,'g-')
	plt.plot(np.arange(len(vol_std_values))[outlier],vol_std_values[outlier],'o', color = 'r')
	lower = dig.iqr_outliers(vol_std_values)[1][0]
	upper = dig.iqr_outliers(vol_std_values)[1][1]
	plt.axhline(y = lower,color = 'b')
	plt.axhline(y = upper, color = 'r')
	plt.xlabel('voxel')
	plt.ylabel('std')
	plt.title('std of each voxel')
	plt.legend(['std','outlier','lower threshold','higher threshold'],loc = 4)

def plot_rmsd(rms_values):

plt.plot(np.arange(len(rms_values)),rms_values,'g-')
plt.plot(np.arange(len(rms_values))[vol_rms_outliers],rms_values[vol_rms_outliers],'o', color = 'r')
lower = dig.iqr_outliers(rms_values)[1][0]
upper = dig.iqr_outliers(rms_values)[1][1]
plt.axhline(y = lower, color = 'b')
plt.axhline(y = upper, color = 'r')
plt.xlabel('voxel')
plt.ylabel('rmsd')
plt.title('rmsd of each voxel')
plt.legend(['rmsd','outlier','lower threshold','higher threshold'],loc = 1)


 
def plot_extend_diff_outliers(new_rms_values):

plt.plot(np.arange(len(new_rms_values)),new_rms_values,'g-')
plt.plot(np.arange(len(new_rms_values))[extended_indices],new_rms_values[extended_indices],'o', color = 'r')
plt.plot(np.arange(len(new_rms_values))[len(new_rms_values)-1],new_rms_values[len(new_rms_values)-1],'o', color = 'b')

plt.axhline(y = lower, color = 'b')
plt.axhline(y = upper, color = 'r')
plt.xlabel('voxel')
plt.ylabel('rmsd')
plt.title('new rmsd of each voxel')
plt.legend(['new rmsd','outlier','exception','lower threshold', 'higher threshold'],loc = 3)
