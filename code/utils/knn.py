# This file is for k-nearest neighbors

from numpy as np
from sklearn.neighbors import KNeighborsClassifier


def knn(X_train, X_test, y_train, y_test, k = 5):
    """ This function returns test error by using k-nearest neighbors
        
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
        k: int or float (optional)
            the number of sample. The default value is 5.
        
        Returns
        -------
            test_error: float
        test error
        
        """
        knn = KNeighborsClassifier(n_neighbors = k)
        knn.fit(X_train,y_train)
        predicted = knn.predict(X_test)
        test_error = 1 - np.mean(y_test == predicted)
                            
        return test_errortest_error

