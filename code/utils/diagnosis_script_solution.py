""" Script to run diagnostic analysis on FMRI run

The FMRI 'run' is a continuous collection of one or more 3D volumes.

A run is usually stored as a 4D NIfTI image.

In this case we are analyzing the 4D NIfTI image: "ds114_sub009_t2r1.nii"

Fill in the code necessary under the comments below.

As you are debugging, we suggest you run this script from within IPython, with
::

    run diagnosis_script.py

Remember, in IPython, that you will need to "reload" any modules that have
changed.  So, if you have imported your module like this:

    import diagnostics

Then you will need to run this before rerunning your script, to get the latest
version of the code.

    reload(diagnostics)

Before you submit your homework, don't forget to check this script also runs
correctly from the terminal, with::

    python diagnosis_script.py
"""

# import standard libraries here
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
import nibabel as nib

# Load the image as an image object
img = nib.load('ds114_sub009_t2r1.nii')

# Load the image data from the image
data = img.get_data()

# Drop the first four volumes, as we know these are outliers
data = data[..., 4:]

# Use your vol_std function to get the volume standard deviation values for the
# remaining 169 volumes
import diagnostics
vol_stds = diagnostics.vol_std(data)
assert len(vol_stds) == 169

# Write these 169 values out to a text file.
# *IMPORTANT* - this text file MUST be called 'vol_std_values.txt'
np.savetxt('vol_std_values.txt', vol_stds)

# Use the iqr_outlier detection routine to get indices of outlier volumes
# Write these indices out to a text file.
# *IMPORTANT* - this text file MUST be called 'vol_std_outliers.txt'
outliers, thresholds = diagnostics.iqr_outliers(vol_stds)
np.savetxt('vol_std_outliers.txt', outliers)

"""
Plot all these on the same plot:

* The volume standard deviation values;
* The outlier points from the std values, marked on the plot with an 'o'
  marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

Extra points for a good legend to the plot.

Save the figure to the current directory as ``vol_std.png``.

IMPORTANT - use exactly this name.
"""
N = len(vol_stds)
x = np.arange(N)
plt.plot(vol_stds, label='vol std')
plt.plot(x[outliers], vol_stds[outliers], 'o', label='outliers')
plt.plot([0, N], [thresholds[0], thresholds[0]], ':', label='IQR lo')
plt.plot([0, N], [thresholds[1], thresholds[1]], ':', label='IQR hi')
plt.legend()
plt.savefig('vol_std.png')
plt.close()

""" Next calculate and plot the RMS difference values

* Calculate the RMS difference values for the image data;
* Use the ``iqr_outlier`` function to return indices of possible outliers in
  this RMS difference vector;

On the same plot, plot the following:

* The RMS vector;
* The identified outlier points marked with an `o` marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

IMPORTANT - save this plot as ``vol_rms_outliers.png``
"""
rms_dvals = diagnostics.vol_rms_diff(data)
rms_outliers, rms_thresholds = diagnostics.iqr_outliers(rms_dvals)
N = len(rms_dvals)
x = np.arange(N)
plt.plot(rms_dvals, label='vol RMS differences')
plt.plot(x[rms_outliers], rms_dvals[rms_outliers], 'o', label='outliers')
plt.plot([0, N], [rms_thresholds[0], rms_thresholds[0]], ':', label='IQR lo')
plt.plot([0, N], [rms_thresholds[1], rms_thresholds[1]], ':', label='IQR hi')
plt.legend()
plt.savefig('vol_rms_outliers.png')
plt.close()

""" Use the ``extend_diff_outliers`` to label outliers

Use ``extend_diff_outliers`` on the output from ``iqr_outliers`` on the RMS
difference values.  This gives you indices for labeled outliers.

On the same plot, plot the following:

* The RMS vector with a 0 appended to make it have length the same as the
  number of volumes in the image data array;
* The identified outliers shown with an `o` marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

IMPORTANT - save this plot as ``extended_vol_rms_outliers.png``
"""
T = data.shape[-1]
ext_outliers = diagnostics.extend_diff_outliers(rms_outliers)
x = np.arange(T)
rms_dvals_ext = np.concatenate((rms_dvals, (0,)), axis=0)
plt.plot(rms_dvals_ext, label='vol RMS differences')
plt.plot(x[ext_outliers], rms_dvals_ext[ext_outliers], 'o', label='outliers')
plt.plot([0, N], [rms_thresholds[0], rms_thresholds[0]], ':', label='IQR lo')
plt.plot([0, N], [rms_thresholds[1], rms_thresholds[1]], ':', label='IQR hi')
plt.legend()
plt.savefig('extended_vol_rms_outliers.png')
plt.close()

""" Write the extended outlier indices to a text file.

IMPORTANT: name the text file extended_vol_rms_outliers.txt
"""
np.savetxt('extended_vol_rms_outliers.txt', ext_outliers)

""" Show that the residuals drop when removing the outliers

Create a design matrix for the image data with the convolved neural regressor
and an intercept column (column of 1s).

Load the convolved neural time-course from ``ds114_sub009_t2r1_conv.txt``.

Fit this design to estimate the (2) betas for each voxel.

Subtract the fitted data from the data to form the residuals.

Calculate the mean residual sum of squares (MRSS) at each voxel (the sum of
squared divided by the residual degrees of freedom).

Finally, take the mean of the MRSS values across voxels.  Print this value.
"""
convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')
# Drop the first four values of the convolved time course to match data
convolved = convolved[4:]
vol_shape = data.shape[:-1]
X = np.ones((T, 2))
X[:, 0] = convolved
time_by_vox = np.reshape(data, (-1, T)).T
Xp = npl.pinv(X)
beta_hats = Xp.dot(time_by_vox)
residuals = time_by_vox - X.dot(beta_hats)
df = T - npl.matrix_rank(X)
mrss = np.sum(residuals ** 2, axis=0) / df
print(np.mean(mrss))

"""
Next do the exactly the same, except removing the extended RMS difference
outlier volumes from the data and the corresponding rows for the design.

Print the mean of the RMSS values across voxels. Is this value smaller?
"""
good_rows = np.ones(T, dtype=bool)
good_rows[ext_outliers] = False
fX = X[good_rows, :]
f_time_by_vox = time_by_vox[good_rows, :]
fXp = npl.pinv(fX)
beta_hats = fXp.dot(f_time_by_vox)
f_residuals = f_time_by_vox - fX.dot(beta_hats)
df = fX.shape[0] - npl.matrix_rank(fX)
f_mrss = np.sum(f_residuals ** 2, axis=0) / df
print(np.mean(f_mrss))

""" Now save these two mean MRSS values to a text file

IMPORTANT: save to ``mean_mrss_vals.txt``
"""

np.savetxt('mean_mrss_vals.txt', (np.mean(mrss), np.mean(f_mrss)))

# Some final checks that you wrote the files with their correct names
from os.path import exists
assert exists('vol_std_values.txt')
assert exists('vol_std_outliers.txt')
assert exists('vol_std.png')
assert exists('vol_rms_outliers.png')
assert exists('extended_vol_rms_outliers.png')
assert exists('extended_vol_rms_outliers.txt')
assert exists('mean_mrss_vals.txt')
