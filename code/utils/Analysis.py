from design_matrix import *
from t import *
from correlation import *
import numpy as np
import matplotlib.pyplot as plt


Betas_vol = {'Beta_vols'+str(x): design_matrix('sub001', x, TR = 2.5)[2] for x in range(1,13)}


#1 House vs face
hf = t_map(Betas_vol,1,8)
plt.imshow(hf[:,:,45])
plt.colorbar()
plt.title('House vs Face')
plt.savefig('../../images/house_vs_face.png', dpi = 100)
plt.close()

#2 House vs every other category regressor
for i in range(2,9):
	plt.subplot(4,2,i-1)
	plt.tight_layout()
	fix = t_map(Betas_vol,1,i)
	plt.imshow(fix[:,:,45])
	plt.clim(-3,6)
	plt.title(str(i))
	plt.colorbar()
plt.savefig( "../../images/house_everything.png", dpi = 100)
plt.close()

######3 cat vs scram
cat_s = t_map(Betas_vol,3,2)
plt.imshow(cat_s[:,:,45])
plt.title('Cat vs scram')
plt.colorbar()
plt.savefig( "../../images/cat_vs_scram.png", dpi = 100)
plt.close()
########4 cat vs shoe
cat_shoe = t_map(Betas_vol,3,4)
plt.imshow(cat_shoe[:,:,45])
plt.title('Cat vs shoe')
plt.colorbar()
plt.savefig( "../../images/cat_vs_shoe.png", dpi = 100)
plt.close()

##5 Cat vs every other category regressor
for i in np.concatenate((range(1,3), range(4,9))):
	plt.subplot(4,2,i-1)
	plt.tight_layout()
	fix = t_map(Betas_vol,3,i)
	plt.imshow(fix[:,:,45])
	plt.clim(-5,3)
	plt.title(str(i))
	plt.colorbar()

plt.savefig( "../../images/cat_everything.png", dpi = 100)
plt.close()


#6 Correlation: House vs every other categories
correlation = difference_corr(Betas_vol['Beta_vols1'], 1)
plt.imshow(correlation, interpolation = 'nearest')
plt.colorbar()
plt.title("Correlation of House vs everything category")
plt.savefig('../../images/corr_House_vs_everything.png')
plt.close()

#correlation7 all(run1)

for i in range(1,9):
	plt.subplot(4,2,i)
	plt.tight_layout()
	correlation = difference_corr(Betas_vol['Beta_vols1'], i)
	plt.imshow(correlation, interpolation = 'nearest')
	plt.title(str(i))
	plt.clim(-0.15,1)
	plt.colorbar()

plt.savefig("../../images/correlation_difference.png", dpi = 100)
plt.close()


