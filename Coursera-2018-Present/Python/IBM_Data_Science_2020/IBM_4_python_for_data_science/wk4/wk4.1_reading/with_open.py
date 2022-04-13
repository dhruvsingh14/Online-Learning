#############################################
# reading in txt files using 'with' command #
#############################################

# a better way to read in files is using the 'with' command
example1 = r"C:\Users\drewn\Desktop\python_for_data_science-master\wk4\example1.txt"

# using with to store and print contents
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# closes file automatically
print(file1.closed)

# stored data remains
print(FileContent)

############################################
# now reading through characters piecewise #
############################################
# read first 4 characters
with open(example1, "r") as file1:
    print(file1.read(4))

# eg 1 read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# each successive call prints the next string, starting from where it ended printing
# eg 2 of piecewise read
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

#######################################
# now reading through lines at a time #
#######################################
# reading one line at a time
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# using a loop to iterate through each line
with open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1;
# in this way we can print pieces of strings without concatenating

# readlines, note plural with an s, saves to a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# printing lines using index referencing
print(FileasList[0])

# printing second line using relevant index
print(FileasList[1])

# printing third line with indexing
print(FileasList[2])

########
# quiz #
########
with open(example1, "r") as file1:
    FileContent=file1.read()
    print(FileContent)
