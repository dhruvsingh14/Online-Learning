#############################################
# Assignment 2: Part 1, Regression Analysis #
#############################################

####################
# Q6: starter code #
####################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


mush_df = pd.read_csv('readonly/mushrooms.csv')
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:,2:]
y_mush = mush_df2.iloc[:,1]

# use the variables X_train2, y_train2 for Question 5
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)

# For performance reasons in Questions 6 and 7, we will create a smaller version of the
# entire mushroom dataset for use in those questions.  For simplicity we'll just re-use
# the 25% test split created above as the representative subset.
#
# Use the variables X_subset, y_subset for Questions 6 and 7.
X_subset = X_test2
y_subset = y_test2

######
# Q6 #
######

# starter code
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

##################
# Assignment Q 6 #
##################

# logarithmic cutpoints for gamma
param_range = np.logspace(-4, 1, 6)

# validation curve
train_scores, test_scores = validation_curve(SVC(), X_subset, y_subset,
                                            param_name='gamma',
                                            param_range=param_range, cv=3)

# svc classifier
model = SVC(kernel='rbf', C=1)
model.fit(X_train2, y_train2)

# svc accuracy for each gamma
for this_gamma in [0.0001, 0.001, 0.01, 0.1, 1, 10]:
    clf = SVC(kernel = 'rbf', gamma = this_gamma).fit(X_train2, y_train2)

# storing training scores and test scores
training_scores = train_scores.mean(axis=1)
test_scores = test_scores.mean(axis=1)

# printing tuple
tuple = (training_scores, test_scores)

print(tuple)

######
# Q7 #
######

# casting gamma and accuracy scores to dataframe
df_gamma_acc = pd.DataFrame([0.0001, 0.001, 0.01, 0.1, 1, 10], columns=['Gamma'])
df_gamma_acc['Accuracy_train'] = tuple[0]
df_gamma_acc['Accuracy_test'] = tuple[1]

df_gamma_acc = df_gamma_acc.set_index('Gamma')

plt.plot(df_gamma_acc['Accuracy_train'], '-o')
plt.plot(df_gamma_acc['Accuracy_test'], '-o')
plt.legend(['train', 'test'])
plt.show()



## soo it is clear that a gamma of 0.1 has a superior performance
## with an accuracy of 1

## a gamma of 0.0001 underfits the model

## while a gamma of 10 overfits















# plt.show() to display plots
