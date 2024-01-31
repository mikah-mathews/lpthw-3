print("Choices are made by entering the numbers '1' or '2'")
print("You wake up in a dim room. You have no memory of how you got here.")
print("Water drips in the distance; the room smells of mildew and rot.")
print("1. Look around for clues")
print("2. Yell for help")

choice1 = input("> ")

if choice1 == "1":
    print("You get up and pace around the room.")
    print("Feeling the walls ends up leading you to discover a hidden doorway to a tunnel.")
    print("1. Enter the tunnel")
    print("2. Yell down the tunnel")
    doorway = input("> ")

elif choice1 == "2":
    print("Your voice echoes around the room as you raise your voice.")
    print("In the distance you hear someone call back.")
    print("A part of the ceiling slides open and a ladder drops to the floor.")
    print("1. Climb the ladder")
    print("2. Look for a weapon")

else:
    print("A trapdoor opens up beneath your feet and you fall into a pit of lava.")