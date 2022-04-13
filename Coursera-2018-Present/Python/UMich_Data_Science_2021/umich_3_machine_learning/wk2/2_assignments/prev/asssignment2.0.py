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

# You can use this function to help you visualize the dataset by
# plotting a scatterplot of the data points
# in the training and test sets.
def part1_scatter():
    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(X_train, y_train, label='training data')
    plt.scatter(X_test, y_test, label='test data')
    plt.legend(loc=4)
    plt.show();

part1_scatter()



#
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Your code here:

# note: brainstorming
# reshaping data from 1D to 2D arrays
# to fit with below functions


x = x.reshape(-1, 1)
poly = PolynomialFeatures(degree=3)

x_poly = poly.fit_transform(x)

# rerunning test train split for transformed data
X_train, X_test, y_train, y_test = train_test_split(x_poly, y, random_state=0)

linreg = LinearRegression().fit(X_train, y_train)

# creating vector of x values to predict vector of y values
# X_predict_input = np.linspace(0, 10, 100).reshape(-1, 1)
X_predict_input = np.linspace((0,0),(10,10),100)

#print(X_predict_input.shape)

# predicting y values vector
y_predict_output = linreg.predict(X_predict_input)

print(X_predict_input[:,0], X_predict_input[:,1], y_predict_output)

plt.scatter(X_predict_input[:, 0], y_predict_output, marker = '^', s = 10,
                 label='Predicted', alpha=0.8)

plt.scatter(X_train[:,0], y_train, marker = 'o', label='True Value', alpha=0.8)

plt.xlabel('Input feature')
plt.ylabel('Target value')
plt.title('Polynomial linear regression (degrees={})'.format(3))

plt.legend()

plt.show()
























# plt.show() to display plots
