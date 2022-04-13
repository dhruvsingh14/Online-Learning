#################################
# writing text files using open #
#################################
with open("example2.txt", "w") as File1:
    File1.write("This is line A\n")
    File1.write("This is line B\n")

# keep in mind that \n is a line break
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# using for loop to write lines out to  a text file
with open("example2.txt", "w") as File1:
    for line in Lines:
        File1.write(line)

# can set mode to appended to write to the existing file without overwriting
with open("example2.txt", "a") as File1:
    File1.write("This is line C")


############################################
# using open write to copy out a text file #
############################################

with open("example1.txt", "r") as readfile:
    with open("example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)


###############################
# lab examples: writing files #
###############################

# writing a line to a files
with open("example2.txt", "w") as writefile:
    writefile.write("This is line A")
# checking if it worked without manually clicking
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())

# writing multiple Lines
with open("example2.txt", "w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
# checking whether results hold
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())

# setting mode to appended
with open("example2.txt", "a") as testwritefile:
    testwritefile.write("This is line C\n")
# verifying result
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())

# writing a list of line to txt as follows
# creating list
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# actually trasferring list to text
with open("example2.txt", "w") as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# verifying whether the list was written out effectively
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())

# appending instead
with open("example2.txt", "a") as testwritefile:
    testwritefile.write("This is line D\n")
# verifying append results
with open("example2.txt", "r") as testwritefile:
    print(testwritefile.read())


###############################
# lab examples: copying files #
###############################
# copying example 2 to example 3
with open("example2.txt", "r") as readfile:
    with open("example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
# verifying copy results
with open("example3.txt", "r") as testwritefile:
    print(testwritefile.read())

## likewise we can write data into csv and xls files!


########
# quiz #
########
with open("example.txt", "w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open("example2.txt", "r") as readfile:
    with open("example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)
