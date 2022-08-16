def count_to(int_input):
  i = 0
  numbers = []
  while i < int_input:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("What number do you want to count to?")
wait = input('> ')
count_to(int(wait))