# This file is for cross validation

from sklearn.cross_validation import KFold
import numpy as np 


def cross_validation(data, target, method, n_folds = 5):
	""" 
	This function estimates the test error associated with a given statistical learning 
	method in order to evaluate its performance.

	Parameters
    ----------
    data: array
    	predictor variable

    target: array
    	response variable


    classfication_method: function
    	input the classfication method

    n_folds: float
    	 randomly dividing the set of observations into k groups
    	 the default value is 5

    Returns
    -------
    cv_scores: float

    """

    # Divide the set of observations in to k groups
    cv = KFold(n = len(data), n_folds)

    cv_scores = []

    # Seperate training set and test set, and then estimate the test error 
    for train , test in cv
    	method.fit(data[train], target[train])
    	predicted = method.predict(data[test])
    	cv_scores.append(np.mean(predicted == target[test]))

    return cv_scores

