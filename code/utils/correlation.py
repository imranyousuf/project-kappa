import numpy as np 


def difference_corr(beta, category):
	""" This functions return the correlation matrix of the two categories

	Parameters
	----------
	beta:4D dimensions
		brain activation

	category:
		choose a category to fix it.

	return
	------
	correlation: 2D 
		correlation matrix

	"""

	difference = []

	for i in np.concatenate((range(category-1), range(category ,8))):
		difference.append((beta[...,i]-beta[...,category-1]).reshape([-1]))

	difference = np.array(difference)

	correlation = np.zeros((7,7))
	for j in range(7):
		for k in range(7):
			correlation[j,k] = np.corrcoef(difference[j],difference[k])[1,0]

	return correlation