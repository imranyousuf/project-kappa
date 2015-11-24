# This file is for random forest

import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cross_validation import cross_val_score

X = data
y = target

# Train on 70% of the data, test on the remaining 30%
test_size = 0.3 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

# Create the random forest model

clf = RandomForestClassifier()
# I will change the n_estimators when I get the data. 
# n_estimator depends on data size. n_estimators is default in this case.

clf = clf.fit(X_train, y_train)

predicted = clf.predicte(X_test)

test_errors = 1 - np.mean(y_test == predicted)

# cross-validation of random forest

scores = cross_val_score(clf, X, y)

cv_test_errors = 1 - scores.mean()

cv_test_errors

# We will change some parameters when get data.
# We want to check whether some parameters influence the test error. 