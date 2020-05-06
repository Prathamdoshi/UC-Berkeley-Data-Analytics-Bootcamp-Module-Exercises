instructions ="""
# Netflix lookup

Finding the info to some of netlfix's most popular videos

## Instructions

* Prompt the user for what video they are looking for.

* Search through the `netflix_ratings.csv` to find the user's video.

* If the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

  * For example "Pup Star is rated G with a rating of 82"

* If the CSV does not contain the user's video then print out a message telling them that their video could not be found.
"""

# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
cwd = os.getcwd()
csvpath = os.path.join(cwd, "Python/data/netflix_ratings.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
# Try: Zootopia; Gossip Girl
found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0].lower() == video.lower():
            print(row[0]+ " is rated "+ row[1] + " with a rating of " + row[6])
            found = True
            break

    # If the video is never found, alert the user
    if found == False:
        print("Sorry about this, we don't seem to have what you are looking for!")
