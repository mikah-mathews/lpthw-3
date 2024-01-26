from sys import argv

script, name, age, favorite_color = argv

print('Your name is ', name, 'You\'re ', age, 'years old and your favorite color is', favorite_color)

# I was confused as to why argv was saying that 'name' was the file name then I realized that the first argument for argv
# is always going to be the file/script name.