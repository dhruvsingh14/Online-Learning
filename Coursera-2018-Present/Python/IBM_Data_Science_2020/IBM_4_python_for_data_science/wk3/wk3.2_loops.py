##########################
# wk3.2: Loops in Python #
##########################

#########
# Loops #
#########

#########
# Range #
#########
# Use the range
range(3)

#####################
# What is for loop? #
#####################
# For loop example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])

# Example of for loop
for i in range(0, 8):
    print(i)

# Example of for loop, loop through list
    # declaring variable year here
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

#######################
# What is while loop? #
#######################
# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
print("It took ", i ,"repetitions to get out of loop.")

#################
# Quiz on Loops #
#################

# printing i
for i in range(-5,6):
    print(i)

# printing elements
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for type in Genres:
    print(type)

# printing el's
squares=['red', 'yellow', 'green', 'purple', 'blue']
for col in squares:
    print(col)

# writing a while loop to check ratings
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
j = 0
rating = PlayListRatings[0] #this was crucial
while(rating >= 6):
    rating = PlayListRatings[j]
    j = j + 1
    print(rating)
print("It took ", j ,"repetitions to get out of loop.")

# writing a while loop
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
k = 0
col = squares[0] #this was crucial
while (col == "orange"):
    new_squares.extend([col])
    col=squares[k]
    k=k+1
    print(col)

####################
# Week 3: Quiz 3.2 #
####################
# q1
A=[1,2,3]
for a in A:
  print(2*a)

# q2
x=0
while(x<2):
  print(x)
  x=x+1

# q3
for i,x in enumerate(['A','B','C']):
    print(i,2*x)

# q4
for i in range(1,5):
    if (i!=2):
        print(i)




















# in order to display plot within window
# plt.show()
