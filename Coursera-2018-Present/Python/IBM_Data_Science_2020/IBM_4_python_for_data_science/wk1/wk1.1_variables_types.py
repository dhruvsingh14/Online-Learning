######################
# wk1: basics, intro #
######################

############
# comments #
############
# practice on writing comments
print('Hello, Python!') # This line prints a string
# print('Hi')

##########
# errors #
##########
# Print string as error message
# frint("Hello, Python")

# Try to see build in error message
print("Hello, Python")

# Print string and error to see the running order
print("This will be printed")
# frint("This will cause an error")
print("This will NOT be printed")

############
# exercise #
############
print("Hello, world!")
print("Hello, world!") # Print the traditional hello world


#########
# types #
#########
# Integer
11

# Float
2.14

# string
"Hello, Python 101!"

# Type of 12
type(12)

# Type of 2.14
type(2.14)

# Type of "Hello, Python 101!"
type("Hello, Python 101!")

# Type of 12.0
type(12.0)

###########
# integer #
###########
# Print the type of -1
print(type(-1))

# Print the type of 4
type(4)

# Print the type of 0
type(0)

##########
# Floats #
##########
# Print the type of 1.0
type(1.0) # Notice that 1 is an int, and 1.0 is a float

# Print the type of 0.5
print(type(0.5))

# Print the type of 0.56
type(0.56)

# System settings about float type
#sys.float_info

##############
# Converting #
##############
# Verify that this is an integer
type(2)

# integers to floats
# Convert 2 to a float
float(2)

# Convert integer 2 to a float and check its type
type(float(2))

# Casting 1.1 to integer will result in loss of information
int(1.1)

# strings to integers or floats
# Convert a string into an integer
int('1')

# Convert a string into an integer with error
# int('1 or 2 people')

# Convert the string "1.2" into a float
float('1.2')

# numbers to strings
# Convert an integer to a string
str(1)

# Convert a float to a string
str(1.2)

###########
# Boolean #
###########
# Value true
True

# Value false
False

# Type of True
type(True)

# Type of False
type(False)

# Convert True to int
int(True)

# Convert 1 to boolean
bool(1)

# Convert 0 to boolean
bool(0)

# Convert True to float
print(float(True))

###################
# Exercise: Types #
###################
# float type
print(type(6/2))

# int type
print(type(6//2))

############################
# Expression and Variables #
############################

###############
# Expressions #
###############
# Addition operation expression
43 + 60 + 16 + 41

# Subtraction operation expression
50 - 60

# Multiplication operation expression
5 * 5

# Division operation expression
25 / 5

# Division operation expression
25 / 6

# Integer division operation expression
25 // 5

# Integer division operation expression
25 // 6

########################
# Exercise: Expression #
########################
print(160/60)

# Mathematical expression
30 + 2 * 60

# Mathematical expression
(30 + 2) * 60

#############
# Variables #
#############
# Store value into variable
x = 43 + 60 + 16 + 41

# Print out the value in variable
x

# Use another variable to store the result of the operation between variable and value
y = x / 60
y

# Overwrite variable with new value
x = x / 60
x

# Name the variables meaningfully
total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min

# Name the variables meaningfully
total_hours = total_min / 60 # Total length of albums in hours
total_hours

# Complicate expression
total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours

################################################
# Exercise: Expression and Variables in Python #
################################################
# x  = 7
x = 3 + 2 * 2
print(x)

# y = 10
y = (3 + 2) *2
print(y)

# z = 17
z = x + y
print(z)

















# in order to display plot within window
# plt.show()
