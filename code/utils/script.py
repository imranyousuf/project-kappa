from design_matrix import *
from t import *
from corrleation import *
import numpy as np
import matplotlib.pyplot as plt


Betas_vol = {'Beta_vols'+str(x): design_matrix('sub001', x, TR = 2.5)[2] for x in range(1,13)}

##### house
for i in range(2,9):
	plt.subplot(4,2,i-1)
	fixed_house = t_map(Betas_vol,1,i)
	plt.imshow(fixed_house[:,:,45])
	plt.clim(-3,6)
	plt.colorbar()
plt.savefig( "house_everything.png", dpi = 100)

###### cat

for i in np.concatenate((range(1,3), range(4,9))):
	plt.subplot(4,2,i-1)
	fixed_house = t_map(Betas_vol,3,i)
	plt.imshow(fixed_house[:,:,45])
	plt.clim(-5,3)
	plt.colorbar()

plt.savefig( "cat_everything.png", dpi = 100)


for i in range(1, 9):
	correlation = difference_corr(Betas_vol['Beta_vols1'], i)
	plt.imshow(correlation, interpolation = 'nearest')
	plt.colorbar()
	plt.savefig(str(i) + "_correlation.png", dpi = 100)
	plt.close()

###house vs face
hf = t_map(Betas_vol,1,8)
plt.imshow(hf[:,:,45])
plt.close()

# Cat vs
for i in np.concatenate((range(1,3), range(4,9))):
	fixed_house = t_map(Betas_vol,3,i)
	plt.imshow(fixed_house[:,:,45])
	plt.colorbar()
	plt.savefig(str(i) + "_CAT.png", dpi = 100)
	plt.close()