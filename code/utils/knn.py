# This file is for k-nearest neighbors

from numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix



X = data
y = target

# Train on 70% of the data, test on the remaining 30%
test_size = 0.3 

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size)

# k = 1
# Create the model for k =1 
knn = KNeighborsClassifier(n_neighbors = 1)

#fit the model
knn.fit(X_train,y_train)

# Predict the response variable
predicted = knn.predict(X_test)

# Calculate the test error
test_error = 1 - np.mean(y_test == predicted)

# Get more detail information
confusion_matrix(y_test, predicted)
print(classification_report(y_test, predicted))


# k = 5
# Create the model for k = 5 
knn = KNeighborsClassifier(n_neighbors = 5)

#fit the model
knn.fit(X_train,y_train)

# Predict the response variable
predicted = knn.predict(X_test)

# Calculate the test error
test_error = 1 - np.mean(y_test == predicted)

# Get more detail information
confusion_matrix(y_test, predicted)
print(classification_report(y_test, predicted))


# k = 10
# Create the model for k = 10 
knn = KNeighborsClassifier(n_neighbors = 10)

#fit the model
knn.fit(X_train,y_train)

# Predict the response variable
predicted = knn.predict(X_test)

# Calculate the test error
test_error = 1 - np.mean(y_test == predicted)

# Get more detail information
confusion_matrix(y_test, predicted)
print(classification_report(y_test, predicted))