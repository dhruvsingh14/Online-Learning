##################
# wk1.2: strings #
##################

#####################
# What are Strings? #
#####################
# Use quotation marks for defining string
"Michael Jackson"

# Use single quotation marks for defining string
'Michael Jackson'

# Digitals and spaces in string
'1 2 3 4 5 6 '

# Special characters in string
'@#2_#]&*^%$'

# Print the string
print("hello!")

# Assign string to variable
Name = "Michael Jackson"
Name

############
# Indexing #
############
# Print the first element in the string
print(Name[0])

# Print the element on index 6 in the string
print(Name[6])

# Print the element on the 13th index in the string
print(Name[13])

#####################
# Negative Indexing #
#####################
# Print the last element in the string
print(Name[-1])

# Print the first element in the string
print(Name[-15])

# Find the length of string
print(len("Michael Jackson"))

###########
# Slicing #
###########
# Take the slice on variable Name with only index 0 to index 3
Name[0:4]

# Take the slice on variable Name with only index 8 to index 11
Name[8:12]

##########
# Stride #
##########
# Get every second element. The elments on index 1, 3, 5 ...
Name[::2]

# Get every second element in the range from index 0 to index 4
Name[0:5:2]

#######################
# Concatenate Strings #
#######################
# Concatenate two strings
Statement = Name + "is the best"
Statement

# Print the string for 3 times
3 * "Michael Jackson"

# Concatenate strings
Name = "Michael Jackson"
Name = Name + " is the best"
Name

####################
# Escape Sequences #
####################
# New line escape sequence
print(" Michael Jackson \n is the best" )

# Tab escape sequence
print(" Michael Jackson \t is the best" )

# Include back slash in string
print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )

#####################
# String Operations #
#####################
# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Michael Jackson"
Name.find('el')

# Find the substring in the string.
Name.find('Jack')

# If cannot find the substring in the string
Name.find('Jasdfasdasdf')

###################
# Quiz on Strings #
###################
A = "1"
print(A)

B = "2"
print(B)

# concat
C = A + B
print(C)

D = "ABCDEFG"

# stride
E = 'clocrkr1e1c1t'
print(E[::2])

print("\\")

F = "You are wrong"
print(F.upper())

##################
# Wk 1: Quiz 1.2 #
##################
# q1
name = 'Lizz'
print(name[0:2])

# q2
A='1934567'
print(A[1::2])

# q3
print('1'+'2')

# q4
print('hello'.upper())

# q5
Name="ABCDE"
print(Name.find("B"))

# q6
print(str(1+1))
print(type(str(1+1)))

# q7
print("123".replace("12", "ab"))






















# in order to display plot within window
# plt.show()
