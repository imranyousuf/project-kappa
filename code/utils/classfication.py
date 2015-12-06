# This file has classfication methods

import numpy as np
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

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

def lda(X_train, X_test, y_train, y_test):
    """ This function returns test_error by using linear discriminant analysis
        
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
    
    clf = LinearDiscriminantAnalysis()
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    test_error = 1 - np.mean(y_test == predicted)
                            
    return test_error

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


def qda(X_train, X_test, y_train, y_test):
    """ This function returns test_error by using quadratic discriminant analysis
        
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
            
    clf = QuadraticDiscriminantAnalysis()
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    test_error = 1 - np.mean(y_test == predicted)
                            
    return test_error



def randomForest(X_train, X_test, y_train, y_test):
    """ This function returns test_error by using random forest
        
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
    clf = RandomForestClassifier()
    clf = clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    test_error = 1 - np.mean(y_test == predicted)
                            
    return test_error


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
                            
    return test_error