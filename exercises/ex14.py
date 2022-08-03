from sys import argv

script, user_name, user_age = argv
waiting = '..... >'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions. I already know that you are {user_age} years old")
print(f"Do you like me {user_name}?")
likes = input(waiting)

print(f"Where do you live {user_name}?")
lives = input(waiting)

print("What kind of computer do you have?")
computer = input(waiting)

print(f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
""")