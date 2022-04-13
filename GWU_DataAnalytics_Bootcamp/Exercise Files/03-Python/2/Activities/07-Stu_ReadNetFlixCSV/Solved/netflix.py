# Modules
import os
from os import path
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Path
path = "C:/Dhruv/Data/1_Active Courses/1_GWU_DataAnalytics_Bootcamp/Exercise Files/03-Python/2/Activities/07-Stu_ReadNetFlixCSV/Solved"
 
# Set path for file
csvpath = os.path.join(path, "../Resources", "netflix_ratings.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
    else:
        print("Sorry about this, we don't seem to have what you are looking for!")