import numpy as np

def t_test(beta_diffrence):
	""" This return t-value

	Parameters
	----------
	beta_diffrence: 2d array
		this should be the difference between two categories

	Return
	------
	t:list
		This returns t-value
	"""
	t = []
	for i in range(beta_diffrence.shape[-1]):
		t.append(np.mean((beta_diffrence[:,i])) / np.std((beta_diffrence[:,i])))

	return t


def t_map(beta_dictionary, category1, category2):
	""" This function return the difference of the beta between two categories 
	
	Parameters
	----------
	beta_dictionary: dict 
		This dictionary should include 12 betas

	category1 and category2: int
		1:house 2:scramble 3:cat 4:shoe 5:bottle 6:scissors 7:chair 8:face

	Return
	------
	t_difference_3d: 3d array
		this returns t-value for each voxel


	Examples
	--------
	>>> a = np.array([[2,4],[3,6]])
	>>> t_test(a)
	[5.0, 5.0]
	"""

	beta_difference_matrix = []

	for i in beta_dictionary.keys():
		beta_category1_1d = np.ravel(beta_dictionary[i][...,category1-1])
		beta_category2_1d = np.ravel(beta_dictionary[i][...,category2-1])
		difference = beta_category1_1d - beta_category2_1d
		beta_difference_matrix.append(difference)

	beta_difference_matrix = np.array(beta_difference_matrix)
	t_difference = t_test(beta_difference_matrix)
	t_difference_3d = np.reshape(t_difference, (91,109,91))

	return t_difference_3d