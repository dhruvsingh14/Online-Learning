# reading in txt files using open

example1 = "C:\Dhruv\misc\data\python_for_data_science\wk4\example1.txt"
file1 = open(example1, "r")

# checking contents
# print(file1.read())

# print the path of the file
print(file1.name)

# printing the mode of the object, r or w
print(file1.mode)

# reading the file and assigning it to a variable
FileContent = file1.read()
FileContent

# printing file contents
print(FileContent)

# checking file type
type(FileContent)
print(type(FileContent)

# closing file after finishing
file1.close()
