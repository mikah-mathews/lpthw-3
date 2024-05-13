from sys import argv
script, input_number = argv

def print_to_x(x):
    i = 0
    numbers = []
    
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print_to_x(int(input_number))