from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
#removes everything from cursor position to end of file if called w/no specifications
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# .write() only accepts one variable so this combines all the lines into one
total_lines = line1 + "\n" + line2 + "\n" + line3 + "\n"

# updates file with 3 lines
target.write(total_lines)

# after writing a file, the cursor is at the end. to be able to read the file we need to move the cursor to the beginning
target.seek(0)

print("Now we are going to print the updated file.")
print(target.read())

print("And finally, we close it.")
target.close()