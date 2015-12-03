#This file is for PCA

import numpy as np
from sklearn.decomposition import PCA

def principalComponent(data, components = none):
	"""
	This function keeps the important vectors and reduce the dimensional space
	
	Paramater
	---------
	data: 2D array
		2D array data

	Returns
	-------
	new_data: 2D array
		This is a new data after applying PCA

	


	"""
	pca = PCA(n_components = components)
	pca.fit(data)
	new_data = pca.transform(data)
	column = pca.explained_variance_ratio_

	return new_data