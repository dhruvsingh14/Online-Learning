##############
# numpy prep #
##############

# importing libraries
import numpy as np
import matplotlib.pyplot as plt

#############################
# creating a 2d numpy array #
#############################
# creating a list
a = [[11,12,13],[21,22,23],[31,32,33]]

# casting above list to array
A = np.array(a)
A

# checking matrix dimensions
A.ndim
# 2 dimensional array

# 3 by 3 matrix as told by shape command
A.shape

#######################################
# accessing elements of a numpy array #
#######################################
# the following two notations both access the same element
A[1,2]
A[1][2]
# rightmost in the 2nd row from the top

# accessing top left
A[0][0]

# using slicing to subset matrix by position/ indices
A[0][0:2]
A[0:2,2]
# remember in slicing / indexing, the last digit listed in a span isn't included

####################
# basic operations #
####################
# let capital letters represent 2 d arrays, or matrices
X = np.array([[1,0],[0,1]])
X
Y = np.array([[2,1],[1,2]])
Y

# adding X and Y
Z = X + Y
Z

# multiplying 2 d array w. a scalar
Z = 2 * Y
Z

# matrix multiplication
Y = np.array([[2,1],[1,2]])
Y
X = np.array([[1,0],[0,1]])
X

Z = X * Y
Z


# dot product
A = np.array([[0,1,1],[1,0,1]])
A

B = np.array([[1,1],[1,1],[-1,1]])
B

Z = np.dot(A,B)
Z

# calculating sine of Z
np.sin(Z)

# creating a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C

# get the transpose of C
C.T

########
# quiz #
########
# q1
X = np.array([[1,0],[0,1]])
Y = np.array([[0,1],[1,0]])
Z = X + Y
Z

# q2
X = np.array([[1,0,1],[2,2,2]])
out = X[0:2,2]
out

# q3
X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
Z = np.dot(X,Y)
print(Z)






# in order to display plot within window
# plt.show()
