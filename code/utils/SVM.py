# This file is for support vector machine

import numpy as np
from sklearn.svm import SVC


def svm(X_train, X_test, y_train, y_test, method):
    """ This function returns test_error by support vector machine
        
        Parameters
        ----------
        X_train: 2D array
            Training feature data set
        X_test: 2D array
            Test feature data set
        y_train: 1D array
            Training response variable
        y_test: 1D array
            Test response variable
        method: string
            method of algorithms for pattern analysis.
            There are four types of kernel: linear, rbf, polynomial, and sigmoid
        
        Returns
        -------
        test_error: float
            test error
        
        """
        clf = SVC()
        clf.set_params(kernel = method).fit(X_train, y_train)
        predicted = clf.predict(X_test)
        test_error = 1 - np.mean(y_test == predicted)
        
        return test_error



