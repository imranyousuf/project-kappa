# This file is for Logistic regression

import numpy as np
from sklearn.linear_model import LogisticRegression

def lr(X_train, X_test, y_train, y_test):
    """ This function returns test_error by using logistic regression
        
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
        
        Returns
        -------
        test_error: float
            test error
            
    """

    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    predicted = logreg.predict(X_test)
    est_error = 1 - np.mean(y_test == predicted)
                            
    return test_error