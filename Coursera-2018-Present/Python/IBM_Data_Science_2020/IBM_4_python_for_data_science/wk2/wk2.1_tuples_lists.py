##################
# wk2.1: tuples #
##################

##########
# Tuples #
##########
# Create your first tuple
tuple1 = ("disco",10,1.2 )
print(tuple1)

# Print the type of the tuple you created
print(type(tuple1))

############
# Indexing #
############
# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
tuple1[-1]

# Use negative index to get the value of the second last element
tuple1[-2]

# Use negative index to get the value of the third last element
tuple1[-3]

######################
# Concatenate Tuples #
######################
# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

###########
# Slicing #
###########
# Slice from index 0 to index 2
tuple2[0:3]

# Slice from index 3 to index 4
tuple2[3:5]

# Get the length of tuple
len(tuple2)

###########
# Sorting #
###########
# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

################
# Nested Tuple #
################
# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples
NestedT[2][1][0]

# Print the second element in the second nested tuples
NestedT[2][1][1]

# Print the first element in the second nested tuples
NestedT[4][1][0]

# Print the second element in the second nested tuples
NestedT[4][1][1]

##################
# Quiz on Tuples #
##################
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
print(genres_tuple)

# obtaining length
print(len(genres_tuple))

# printing element at index 3
print(genres_tuple[3])

# slicing
print(genres_tuple[3:6])

# first two elements
print(genres_tuple[0:2])

print("disco"[0])

# sorted tuple
C_tuple=(-5, 1, -3)
print(sorted(C_tuple))

################
# wk2.1: lists #
################

#########
# Lists #
#########

############
# Indexing #
############
# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

################
# List Content #
################
# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

###################
# List Operations #
###################
# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]
print(L)

# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10]) # injects list elements into existing list
print(L)

# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10]) # introduces list as a list element
print(L)

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# Use append to add elements to list
L.append(['a','b'])
print(L)

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
print('hard rock'.split())

# Split the string by comma
'A,B,C,D'.split(',')

#######################
# Copy and Clone List #
#######################
# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
print(B)

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

################
# Quiz on List #
################
a_list = [1, 'hello', [1,2,3], 'TRUE']

# returning needed elements
a_list[1]
a_list[1:4]

# concatenating lists
A = [1,'a']
B = [2,1,'d']
A.extend(B)

print(A)

#################
# Wk2: Quiz 2.1 #
#################
print("Wk2: Quiz 2.1")

# q1
tuple1=("A","B","C")
print(tuple1[-1])

# q2
A=((1),[2,3],[4])
print(A[2])

# q3
A=((1),[2,3],[4])
print(A[2][0])

# q4
print('1,2,3,4'.split(','))

# q5
L.append(['a','b'])

# q6
# lists are mutable, tuples are not

# q7
A=["hard rock",10,1.2]
del(A[0])
print(A)

# q8
# cloning vs. copying

# q9
print(len(("disco", 10)))

















# in order to display plot within window
# plt.show()
