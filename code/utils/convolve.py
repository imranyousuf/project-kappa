# This function refers to the lecture of day 
import numpy as np

def convolve(neural_prediction, hrf_at_trs):
	""" This function convolves the neural prediction """

	convolved = np.convolve(neural_prediction, hrf_at_trs)
	n_to_remove = len(hrf_at_trs) - 1
	convolved = convolved[:-n_to_remove]

	return convolved

