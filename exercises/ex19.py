def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man that's enough for a party!")
  print("Get a blanket. \n")

def do_you_want_a_cracker():
  print("Would you like a cracker? Enter y for yes and n for no.")
  response = input('')
  if (response == "y"):
    print("Ok! Here's a cracker!")
  elif (response == "n"):
    print("That's ok, you don't have to have one :)")
  else:
    print("Sorry - that wasn't a valid input. You'll have to re-run the program")


do_you_want_a_cracker();
# print("We can just give the function the numbers directly:")
# cheese_and_crackers(20, 30)

# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do the math inside too:")
# cheese_and_crackers(10 + 25, 5 + 6)

# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)