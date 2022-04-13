##################################
# Assignment 3: Model Evaluation #
##################################

# importing libraries
import numpy as np
import pandas as pd

############################
# Question 5: Starter Code #
############################

# train test split for training classification models
from sklearn.model_selection import train_test_split

df = pd.read_csv('readonly/fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#######################################
# Question 5: Logistic Classification #
#######################################

# from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

# fitting a logistic regression model
lr = LogisticRegression().fit(X_train, y_train)
lr_predicted = lr.predict(X_test)

# probability estimates for fraud
y_proba_lr = lr.fit(X_train, y_train).predict_proba(X_test)

# prt 1: creating a precision recall curve
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, thresholds = precision_recall_curve(y_test, y_proba_lr[:,1])
closest_zero = np.argmin(np.abs(thresholds))
closest_zero_p = precision[closest_zero]
closest_zero_r = recall[closest_zero]

plt.figure()
plt.xlim([0.0, 1.01])
plt.ylim([0.0, 1.01])
plt.plot(precision, recall, label = 'Precision-Recall Curve')
plt.plot(closest_zero_p, closest_zero_r, 'o', markersize = 12, fillstyle = 'none', c='r', mew=3)
plt.title("Precision Recall Curve")
plt.xlabel('Precision', fontsize = 16)
plt.ylabel('Recall', fontsize = 16)
#plt.axes().set_aspect('equal')
plt.show()

# part 2: roc curve
from sklearn.metrics import roc_curve

# roc curve using y test, and probability estimates
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_proba_lr[:,1])

# plotting figure
plt.figure()
plt.xlim([-0.01, 1.00])
plt.ylim([-0.01, 1.01])
plt.plot(fpr_lr, tpr_lr, lw=3)
plt.xlabel('False Positive Rate', fontsize=16)
plt.ylabel('True Positive Rate', fontsize=16)
plt.title('ROC curve', fontsize=16)
plt.plot([0,1], [0,1], color='navy', lw=3, linestyle='--')
#plt.axes().set_aspect('equal')
plt.show()

# precision = 0.75 corresponds to recall of 0.827
recall = 0.827

# true positive rate = 0.926 when false positive rate = 0.16
true_positive_rate = 0.926







































# plt.show() to display plots
