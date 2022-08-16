def count_to(int_input, increment):
  i = 0
  numbers = []
  while i < int_input:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + increment
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("What number do you want to count to?")
count = input('> ')
print("What number do you want to increment by?")
increment = input('> ')
count_to(int(count), int(increment))