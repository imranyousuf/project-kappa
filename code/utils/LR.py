# This file is for Logistic regression

from numpy as np 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression

# Train on 70% of the data, test on the remaining 30%
test_size = 0.3 
X = data
y = target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

# Create the logistic regression model 
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train, y_train)

# predict the response variable
predicted = logreg.predict(X_test)

# Calculate the test error
test_error = 1 - np.mean(y_test == predicted)

test_error

# Get more detail information
confusion_matrix(y_test, predicted)
print(classification_report(y_test, predicted))