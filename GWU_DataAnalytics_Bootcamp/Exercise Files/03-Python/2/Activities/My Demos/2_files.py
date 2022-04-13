# importing libraries
import os

# getting and setting directory
os.getcwd()
os.chdir("C:/Dhruv/Data/1_Active Courses/1_GWU_DataAnalytics_Bootcamp/Exercise Files/03-Python/2/Activities/My Demos")

'''
# reading a text file
f = open('data/description.txt', 'r')
contents = f.read()
print(contents)
f.close()

# writing to a file
f = open('data/description.txt', 'w')
f.write("Yodel grew up in a family of singers and loud talkers and could never get a word in edgewise")
f.close()
'''

# reading a text file
with open('data/description.txt', 'r') as f:
    contents = f.read()
    print(contents)

# writing to a file
with open('data/description.txt', 'w') as f:
    f.write("Yodel grew up in a family of singers and loud talkers and could never get a word in edgewise")
