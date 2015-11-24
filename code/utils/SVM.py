# This file is for support vector machine

import numpy as np 
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

X = data
y = target

# Train on 70% of the data, test on the remaining 30%
test_size = 0.3 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)


# Create the support vector machine model with the default parameter values
clf = SVC()

# fit the train data
clf.fit(X_train, y_train)

# Predict the response variable
predicted = clf.predict(X_test)

#calculate the test error
test_error = 1 - np.mean(y_test == predicted)

test_error

# get the detail information
print(classification_report(y_test, predicted))
confusion_matrix(y_test, predicted)


# Create the support vector machine model with the linear kernal and fit the data
clf = SVC()
clf.set_params(kernel='linear').fit(X_train, y_train) 

# Predict the response variable
predicted = clf.predict(X_test)

#calculate the test error
test_error = 1 - np.mean(y_test == predicted)

test_error

# get the detail information
print(classification_report(y_test, predicted))
confusion_matrix(y_test, predicted)



# create the support vector machine model with the radial kernel kernal and fit the data
clf = SVC()
clf.set_params(kernel='rbf').fit(X_train, y_train) 

# Predict the response variable
predicted = clf.predict(X_test)

#calculate the test error
test_error = 1 - np.mean(y_test == predicted)

test_error

# get the detail information
print(classification_report(y_test, predicted))
confusion_matrix(y_test, predicted)



