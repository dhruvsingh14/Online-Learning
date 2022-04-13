#############################################
# Assignment 2: Part 1, Regression Analysis #
#############################################

# importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# creating simulated data
np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

# test train split
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

######
# Q4 #
######

# importing libraries
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics import r2_score

# calling global variables
# global X_train, X_test

# reshaping x train to transform into x train poly
X_train = X_train.reshape(-1, 1)
# reshaping x test to transform into x test poly
X_test = X_test.reshape(-1, 1)

# x train: polynomial transformation, degree 12
poly = PolynomialFeatures(degree=12)
x_train_poly = poly.fit_transform(X_train)
# x test: polynomial transformation, degree 12
x_test_poly = poly.fit_transform(X_test)

# Model 1: fitting linear regression model to training data
model = LinearRegression()
model.fit(x_train_poly, y_train)


# predicting y values using training data
y_test_poly_pred = model.predict(x_test_poly)

print(y_test.shape)
print(y_test_poly_pred.shape)


# scoring linear regression model for training data, and storing performance score
LinearRegression_R2_test_score = r2_score(y_test, y_test_poly_pred)


# Model 2: fitting lasso regression model to training data
linlasso = Lasso(alpha=0.01, max_iter=10000).fit(x_train_poly, y_train)
# scoring lassos regression model for training data, and storing performance score
Lasso_R2_test_score = linlasso.score(x_train_poly, y_train)


print(LinearRegression_R2_test_score, Lasso_R2_test_score)
































# plt.show() to display plots
