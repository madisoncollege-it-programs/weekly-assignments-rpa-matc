#!/usr/bin/env python3 

print("""You enter a dark room with three doors. 
Do you go through door #1, door #2 or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a chest full of gold.")
    print("What do you do?\n")

    print("1. Take the chest.")
    print("2. Leave the chest.")

    # == Chest logic ============================
    Chest = input("-> ")

    if Chest == "1":
        print("1) The chest is booby trapped and you die from the trap!")
    elif Chest == "2":
        print("2) You survive with your life, but lost all the gold!")
    else:
        print("Well, taking some gold is probably better.")
        print("You leave and lost your chance of living the dream.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("There's a skeleton holding a goldden crown.\n")

    print("1. Take the crown.")
    print("2. Leave the crown.")
    print("3. Take the whole skeleton???")

# == Crown Logic ======================
    Crown = input("-> ")

    if Crown == "1":
        print("1) You have the crown in your hands, but begin to feel sleepy")
        print("You fall next to the skeleton and hold the crown. You then fall asleep and become the next skeleton.")
    elif Crown == "2":
        print("2) You have lost the crown and leave with nothing but your life.")
    else:
        print("N) You put the skeleton in a bag along with the crown and leave the cave.")
        print("N) Upon returning home you cash in the crown and hide the skeleton and live a life of luxury!")

# == Door Number 3 Logic ====================
elif door =="3":
    print ("You enter Thanos' room and find the infinity gauntlet with all of the infinity stones.\n")

    print ("1. take the gauntlet.")
    print ("2. Leave the gauntlet.")
    print ("3. use the gauntlet...?")
# == Gauntlet Logic =====================
    Gauntlet = input("->")

    if Gauntlet == "1":
        print("1) You take the gauntlet back home and keep it as a trophy hidden from the rest of the world")
        print("Thanos realizes the gauntlet is missing and destroys the solar system trying to find it.")
    elif Gauntlet == "2":
        print("You leave the gauntlet and save the solar system becoming a hero without knowing it.")
    else:
        print("N) You use the Infinity Gauntlet and snap your fingers, you begin to feel a change in the air and see everything around you turn into dust including  yourslef.")
else:
    print("you didn't choose a door??? Good choice :)")
