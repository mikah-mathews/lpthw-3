# imports argv module from sys
from sys import argv

# sets the 2 arguments, we will use the second to grab the txt file to read
script, filename = argv

# set a variable to retrieve and open file
txt = open(filename)

# prints the name of txt file 
print(f"Here's your file {filename}:")
# prints contents of txt file
print(txt.read())

txt.close()

# print statement to let users know what they should do next
# print("Type the filename again:")
# # gets name of txt file that user wants to use
# file_again = input("> ")

# # returns file object
# txt_again = open(file_again)

# # prints output of .read() function on file object
# print(txt_again.read())