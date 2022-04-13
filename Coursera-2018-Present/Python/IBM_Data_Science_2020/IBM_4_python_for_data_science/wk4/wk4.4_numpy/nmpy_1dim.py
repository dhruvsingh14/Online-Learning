##############
# numpy prep #
##############

# importing numpy
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# plotting functions

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2,2)
    plt.xlim(-2,2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color = 'r', head_length=0.1)
    ax = plt.axes()
    ax.arrow(0, 0, *b, head_width=0.05, color = 'b', head_length=0.1)
    plt.ylim(-2,2)
    plt.xlim(-2,2)

# creating a python list:
a = ["0", 1, "two", "3", 4]

# can print each element as follows:
#print("a[0]", a[0])
#print("a[1]", a[1])
#print("a[2]", a[2])
#print("a[3]", a[3])
#print("a[4]", a[4])

###############################
# numpy: what is it good for? #
###############################
# creating an array in numpy, separate from regular py arrays
a = np.array([0, 1, 2, 3, 4])
a

# can print numpy arrays in much the same way
#print("a[0]:", a[0])
#print("a[1]:", a[1])
#print("a[2]:", a[2])
#print("a[3]:", a[3])
#print("a[4]:", a[4])

###################
# addressing type #
###################
type(a)

# checking element types: equiv of str in r
a.dtype

# creating a new numpy array with float types
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# checking array type
type(b)

# checking element types
b.dtype

####################
# assigning values #
####################

# create numpy array
c = np.array([20, 1, 2, 3, 4])
c

# changing the value of element 1 through assignment
c[0] = 100
c

# assigning element 5 a value of 0
c[4] = 0
#print(c)

###########
# slicing #
###########

d = c[1:4]
d

# replacing array c's values using colon shorthand
c[3:5] = 300, 400
c
# [100   1   2 300 400]
# basically the colon shorthand is called slicing

################################
# assigning values using lists #
################################

# creating the list of indices to be assigned
select = [0, 2, 3]

# using above list to select elements or subset
# using c+index list to replace values of d
d = c[select]
d

# using values to assign to index list
c[select] = 100000
c

####################
# other attributes #
####################

# once again, creating a numpy array
a = np.array([0, 1, 2, 3, 4])
a
# now working to display dim functionality in py
# getting size of numpy arrays
a.size
# note: numpy functionality only works on numpy arrays
# getting the numer of dimensions of a numpy array
a.ndim
# getting the shape and size of the numpy array
a.shape
# note: you have to explicitly print any object in script unlike in notebooks


# creating a numpy array
a = np.array([1, -1, 1, -1])
# getting the mean of the array
mean = a.mean()
mean
# getting the std dev of the array
standard_deviation = a.std()
standard_deviation


# creating a numpy array
b = np.array([-1, 2, 3, 4, 5])
b

# getting the biggest value in the numpy array
max_b = b.max()
max_b

# conversely, getting the lowest value
min_b = b.min()
min_b


##########################
# numpy array operations #
##########################

##################
# array addition #
##################
u = np.array([1,0])
u

v = np.array([0,1])
v

# numpy array addition
z = u + v
z

# plot numpy arrays
Plotvec1(u, z, v)
#plt.show()

#########################
# array multiiplication #
#########################
y = np.array([1,2])
y

# numpy array multiiplication
z = 2 * y
z

###############################
# product of two numpy arrays #
###############################
u = np.array([1,2])
u

v = np.array([3,2])
v

# calculate the product of two numpy arrays
z = u * v
z

###############
# dot product #
###############
np.dot(u,v)

u = np.array([1,2,3,-1])
u

##################################
# adding a constant to the array #
##################################
u + 1

##########################
# mathematical functions #
##########################
# printing out value of pi
np.pi

# translating array elements values listed in pi to radians
x = np.array([0,np.pi/2,np.pi])

# calculates the sine of each element
y = np.sin(x)
y

############
# linspace #
############
# declaring an equally spaced array, specifying cutpoints, and n
np.linspace(-2,2,num=5)
np.linspace(-2,2,num=9)

# using pi instead for cutpoints
x = np.linspace(0, 2*np.pi, num=100)

# calculate the sine of x list
y = np.sin(x)

# plot the result
#plt.plot(x,y)
#plt.show()
# spliced from line due to sinusoidal nature

##########################
# quiz on 1d numpy array #
##########################

# declaring arrays
u = np.array([1,0])
v = np.array([0,1])

# calculating the difference
u-v

# declaring and multiplying by a scalar
z = np.array([2,4])
z*-2

# casting lists to arrays
x = np.array([1,2,3,4,5])
y = np.array([1,0,1,0,1])
x*y

# converting lists to numpy arrays
a = np.array([-1,1])
b = np.array([1,1])
# plotting arrays as vectors
#Plotvec2(a,b)
#plt.show()
# dot product
np.dot(a,b)

# doing the same for the following lists
a = np.array([1,0])
b = np.array([0,1])
#Plotvec2(a,b)
#plt.show()
np.dot(a,b)

# doing the same for the following lists
a = np.array([1,1])
b = np.array([0,1])
#Plotvec2(a,b)
#plt.show()
np.dot(a,b)

# perpendicular vectors above give a 0 dot product


########
# quiz #
########
#q1
a = np.array([0,1,0,1,0])
b = np.array([1,0,1,0,1])
print(a*b)

# q2
a = np.array([-1,1])
b = np.array([1,1])
print(np.dot(a,b))

# q3
a = np.array([1,1,1,1,1])
print(a + 10)

















# in order to display plot within window
# plt.show()
