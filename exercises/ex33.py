from sys import argv
script, count_to, increment_by = argv

def print_to_x(x, y):
    i = 0
    numbers = []
    
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    # create for-loop to print numbers
    for num in numbers:
        print(num)

print_to_x(int(count_to), int(increment_by))