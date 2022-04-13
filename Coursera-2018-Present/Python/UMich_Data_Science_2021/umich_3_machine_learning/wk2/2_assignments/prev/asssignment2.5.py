#############################################
# Assignment 2: Part 1, Regression Analysis #
#############################################

######
# Q5 #
######

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

from sklearn.tree import DecisionTreeClassifier


# Q5

# fitting classifier model
clf = DecisionTreeClassifier().fit(X_train2, y_train2)

# setting tree depth
clf2 = DecisionTreeClassifier(max_depth = 3).fit(X_train2, y_train2)

# storing feature importance
feature_importance = clf.feature_importances_

# converting array to dataframe
feature_importance = pd.DataFrame(feature_importance)

# attaching feature names
feature_importance['feature_names'] = X_train2.columns

# renaming columns
feature_importance.columns = ['feature_importance', 'feature_name']

# sorting and storing most important features
top5_features = feature_importance.sort_values(by = ['feature_importance'], ascending=False).head()

# saving to list
top5_features_list = top5_features["feature_name"].tolist()

# return list
print(top5_features_list)


# plt.show() to display plots
