from sys import argv

script, name, age, favorite_color = argv

animal = input("What is your favorite animal? ")

print('Your name is ', name, 'You\'re ', age, 'years old, your favorite color is', favorite_color, 'and your favorite animal is', animal)

# I was confused as to why argv was saying that 'name' was the file name then I realized that the first argument for argv
# is always going to be the file/script name.