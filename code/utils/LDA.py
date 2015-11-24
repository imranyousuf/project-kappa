# This file is for linear discriminant analysis

import numpy as np 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


X = data
y = target

# Train on 70% of the data, test on the remaining 30%
test_size = 0.3 

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size)

# Create the support linear discriminant analysis
clf = LinearDiscriminantAnalysis()

# fit the train data
clf.fit(X_train, y_train)

# Predict the response variable
predicted = clf.predict(X_test)

#calculate the test error
test_error = np.mean(y_test == predicted)

# get the detail information
print(classification_report(y_test, predicted))
confusion_matrix(y_test, predicted)

