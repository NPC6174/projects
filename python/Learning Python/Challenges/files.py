#
# Files Challenge
# Create a program that creates a new directory,
# creates a text file within that directory, 
# and writes into that file the listing of all the files in the current directory,
# along with the total byte count of all those files.
#

import os

totalbytes = 0

# Get a list of all the files in the current directory
dirlist = os.listdir()
for entry in dirlist:
# Make sure it's a file!
    if os.path.isfile(entry):
# Add the file size to the total
        filesize = os.path.getsize(entry)
        totalbytes += filesize

# Create a subdirectory called "results"
os.mkdir("results")

# Create the output file
resultsfile = open("results/results.txt", "w+")
if resultsfile.mode == "w+":
        resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
        resultsfile.write("Files list:\n")
        resultsfile.write("--------------\n")
# Write the results into the file
        for entry in dirlist:
            if os.path.isfile(entry):
# Write the file name to the results ledger
                resultsfile.write(entry + "\n")
# Close the file when done
        resultsfile.close()