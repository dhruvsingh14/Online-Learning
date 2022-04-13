###############################################
# Assignment 4: Urban Blight Prediction Model #
###############################################

# importing libraries
import numpy as np
import pandas as pd

#############
# Data Prep #
#############

# reading in all data files
train = pd.read_csv('readonly/train.csv')
test = pd.read_csv('readonly/test.csv')
addresses = pd.read_csv('readonly/addresses.csv')
latlons = pd.read_csv('readonly/latlons.csv')

# splitting data into target var and predictors
X_train = train.iloc[:,:-1]
y_train = train.iloc[:,-1]

###########
# Merging #
###########

# setting indices to ticket id
X_train = X_train.set_index('ticket_id')
addresses = addresses.set_index('ticket_id')

# merging on ticket id
X_train = pd.merge(X_train, addresses, how = 'inner',
                    left_index=True, right_index=True)

# resetting index, to keep ticket id from being overwritten
# X_train = X_train.reset_index()

# setting address to lower case, then index for merge
X_train['address'] = X_train['address'].str.lower()
X_train = X_train.set_index('address')

latlons['address'] = latlons['address'].str.lower()
latlons = latlons.set_index('address')

# merging on address
X_train = pd.merge(X_train, latlons, how = 'inner',
                    left_index=True, right_index=True)

################################
# Model 1: Logistic Regression #
################################

from sklearn.linear_model import LogisticRegression

# fitting a logistic regression model
lr = LogisticRegression().fit(X_train, y_train)
lr_predicted = lr.predict(X_test)

# probability estimates for blight
y_proba_lr = lr.fit(X_train, y_train).predict_proba(X_test)






'''
X_train
X_test
y_train
y_test

###########################
# Question 6: Grid Search #
###########################

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# declaring a logistic regression model
clf = LogisticRegression()

# range of candidate penalty
penalty = ['l1', 'l2']

# range of regularization
C = np.logspace(-2, 2, 5)

# dictionary of hyperparameter
param_grid = dict(C=C, penalty=penalty)

# using recall for scoring
# grid search: 3 fold cross validation
grid_clf_rec = GridSearchCV(clf, param_grid, cv = 3, scoring='recall')

# fitting grid search
grid_clf_rec.fit(X_train, y_train)

# scoring fitted model
y_decision_fn_scores_rec = grid_clf_rec.decision_function(X_test)

# storing results to dictionary
my_dict = grid_clf_rec.cv_results_

# converting dictionary to dataframe
df = pd.DataFrame.from_dict(my_dict)

# subsetting relevant columns
df = df[['param_C', 'param_penalty', 'mean_test_score']]

# filling na for reshaping
df['mean_test_score'] = df['mean_test_score'].fillna(0)

# reshaping data long to wide
df_w = df.pivot_table(index=["param_C"], columns = 'param_penalty',
                            values = 'mean_test_score').reset_index()

# replacing original nan's in l1 column
df_w['l1'].replace(0, np.nan, inplace=True)

# storing scores to 5x2 array
scores_array = df_w[['l1', 'l2']].to_numpy()
print(scores_array)
'''


































# plt.show() to display plots
