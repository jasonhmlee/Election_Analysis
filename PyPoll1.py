print("hi")

# Add our dependencies.
import csv
import os

#path = os.path.join("/users/jasonlee/Documents/Berkeley_Bootcamp/Election_Analysis/Resources","election_results.csv)
#print(path)

# Add a variable to load a file from a path.
#file_to_load = os.path.join("../Resources/election_results.csv")

# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open("../Resources/election_results.csv","r") as election_data:

    # Print the file object.
     print(election_data.readlines())

print(os.getcwd())




#Write code with OPEN and CLOSE statments
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()


#Write code using WITH statment
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello World")
         # Write three counties to the file.
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

    # Write three counties in each line.
    txt_file.write("\nArapahoe\nDenver\nJefferson")

    print("hi")