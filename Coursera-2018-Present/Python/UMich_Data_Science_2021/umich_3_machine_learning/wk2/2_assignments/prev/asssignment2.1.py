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


#############################################
# Question 1: Polynomial Regression Models #
#############################################
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

'''
# transforming x train to obtain x train poly
X_train = X_train.reshape(-1, 1)
poly = PolynomialFeatures(degree=3)
x_train_poly = poly.fit_transform(X_train)
print(x_train_poly.shape)

# transforming x test to obtain x test poly
X_test = X_test.reshape(-1, 1)
x_test_poly = poly.fit_transform(X_test)
print(x_test_poly.shape)

# note: training and test data must always have the same number of column
# by default. if not, soomething's wrong with the workflow

# training model using polynomial regression
model = LinearRegression()
model.fit(x_train_poly, y_train)

# creating vector of x values to predict y values
x_predict = np.linspace(0, 10, 100).reshape(-1, 1)
x_predict_poly = poly.fit_transform(x_predict)
print(x_predict_poly.shape)

# predicting y values vector
y_poly_pred = model.predict(x_predict_poly)
print(y_poly_pred.shape)

print(y_poly_pred)
# ok so my predictions for degree 3 are on point
# just have to loopify this now.

# creating container to store different scores
deg_3 = []

deg_3.append(y_poly_pred)

print(deg_3)
'''

# deg_1, deg_3, deg_6, deg_9 = [], [], [], []

d = {}

# reshaping x train to transform into x train poly
X_train = X_train.reshape(-1, 1)
# reshaping x test to transform into x test poly
X_test = X_test.reshape(-1, 1)

for k in [1, 3, 6, 9]:
    # transforming x train to obtain x train poly
    poly = PolynomialFeatures(degree=k)
    x_train_poly = poly.fit_transform(X_train)

    # transforming x test to obtain x test poly
    x_test_poly = poly.fit_transform(X_test)

    # training model using polynomial regression
    model = LinearRegression()
    model.fit(x_train_poly, y_train)

    # creating vector of x values to predict y values
    x_predict = np.linspace(0, 10, 100).reshape(-1, 1)
    x_predict_poly = poly.fit_transform(x_predict)

    # predicting y values vector
    y_poly_pred = model.predict(x_predict_poly)

    # creating container to store different scores
    d["deg_{}".format(k)] = y_poly_pred

# converting dictionary to dataframe
df = pd.DataFrame.from_dict(d).T

# converting dataframe to array: 4 x 100
pred_array = df.to_numpy()

print(pred_array)
print(pred_array.shape)


import matplotlib.pyplot as plt
# %matplotlib notebook
plt.figure(figsize=(10,5))
plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
for i,degree in enumerate([1,3,6,9]):
    plt.plot(np.linspace(0,10,100), pred_array[i], alpha=0.8, lw=2, label='degree={}'.format(degree))
plt.ylim(-1,2.5)
plt.legend(loc=4)

plt.show()














'''
import matplotlib.pyplot as plt
plt.scatter(np.linspace(0, 10, 100), y_poly_pred, label='predict')
plt.show()
'''




'''
x = x.reshape(-1, 1)


x_poly = poly.fit_transform(x)

# rerunning test train split for transformed data
X_train, X_test, y_train, y_test = train_test_split(x_poly, y, random_state=0)

# creating vector of x values to predict vector of y values

X_predict_input = np.linspace((0,0),(10,10),100)

#print(X_predict_input.shape)


print(X_predict_input[:,0], X_predict_input[:,1], y_predict_output)

plt.scatter(X_predict_input[:, 0], y_predict_output, marker = '^', s = 10,
                 label='Predicted', alpha=0.8)

plt.scatter(X_train[:,0], y_train, marker = 'o', label='True Value', alpha=0.8)

plt.xlabel('Input feature')
plt.ylabel('Target value')
plt.title('Polynomial linear regression (degrees={})'.format(3))

plt.legend()

plt.show()
'''























# plt.show() to display plots
