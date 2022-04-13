##################################
# Assignment 3: Model Evaluation #
##################################

# importing libraries
import numpy as np
import pandas as pd

############################
# Question 1: Starter Code #
############################

# train test split for training classification models
from sklearn.model_selection import train_test_split

df = pd.read_csv('readonly/fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

################################
# Question 2: Dummy Classifier #
################################

from sklearn.dummy import DummyClassifier
from sklearn.metrics import recall_score

# training dummy classifier
dummy_majority = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)

# creating predictions using dummy classifier model
y_dummy_predictions = dummy_majority.predict(X_test)

# evaluation1: scoring model accuracy on test set
accuracy_score = dummy_majority.score(X_test, y_test)

# evaluation2: model recall on test target vs. prediction
recall_score = recall_score(y_test, y_dummy_predictions)

#########################################
# Question 3: Support Vector Classifier #
#########################################

from sklearn.metrics import recall_score, precision_score
from sklearn.svm import SVC

# training support vector classifier with default parameters
svm = SVC(kernel='rbf', C=1).fit(X_train, y_train)

# creating predictions using support vector model
svm_predicted = svm.predict(X_test)

# evaluation1: scoring model accuracy on test set
accuracy_score = svm.score(X_test, y_test)

# evaluation2: model recall on test target vs. prediction
recall_score = recall_score(y_test, svm_predicted)

# evaluation3: model precision on test target vs. prediction
precision_score = precision_score(y_test, svm_predicted)

print(accuracy_score, recall_score, precision_score)


################################
# Question 4: Confusion Matrix #
################################

from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

# training support vector classifier with custom parameters
svm = SVC(kernel='rbf', C=1e9, gamma=1e-07).fit(X_train, y_train)

# creating predictions using support vector model
svm_predicted = svm.predict(X_test)

# setting threshold
svm_predicted_thres = svm_predicted > -220

# evaluation: confusion matrix
confusion = confusion_matrix(y_test, svm_predicted_thres)
print(confusion)












# plt.show() to display plots
