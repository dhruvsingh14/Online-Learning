##################################
# Assignment 3: Model Evaluation #
##################################

# importing libraries
import numpy as np
import pandas as pd

############################
# Question 6: Starter Code #
############################

# train test split for training classification models
from sklearn.model_selection import train_test_split

df = pd.read_csv('readonly/fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

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
















# plt.show() to display plots
