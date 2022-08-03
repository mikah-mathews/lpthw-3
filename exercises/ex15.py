# importing argv to allow functionality
from sys import argv

# initializing our program and that we want to also have a filename to run the program
script, filename = argv

# it will retrieve the text file
txt = open(filename)

# prints the filename
print(f"Here's your file {filename}:")
# prints the file contents retrieved with open
print(txt.read())

# prints out sentence
print("Type the filename again:")
# retrieves user input of what file they would like to open
file_again = input("> ")

# opens file from name retrieved from input
txt_again = open(file_again)

# prints file contents
print(txt_again.read())