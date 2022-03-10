#!/usr/bin/env python3
print ("Name: Russell Pa")
# Midterm Project Jurassic Park
#Not sure why it ask for input multiple times except for "Reboot" / two times for "Shutdown", three times for "Done" and 3 fasle inputs to print the lysine contingency.
password_database = {"Username":"dnedry","Password":"please"}
command_database = {"Reboot":"OK. I will reboot all park systems.","Shutdown":"OK. I will shut down all park systems.","Done":"I hate all this hacker stuff."}
white_rabbit_object = 0
counter = 0

while counter < 3 and white_rabbit_object == 0:
    print ("Username: ")
    input_user = input("-> ")
    print ("Password: ")
    input_password = input("-> ")
    if input_user == password_database.get('Username') and input_password == password_database.get('Password'):
        white_rabbit_object = 1
        print ("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        print ("Please enter a command: Reboot, Shutdown, Done.")
        if input("-> ") == "Reboot":
            print (command_database.get('Reboot'))
        elif input("-> ") == "Shutdown":
            print (command_database.get('Shutdown'))
        elif input("-> ") == "Done":
            print (command_database.get('Done'))
        else:
            print ("The Lysine Contingency has been put into effect.")



    else:
        counter += 1
        if counter == 3:
            print ("You didn't say the magic word!\n"*25)
        else:
            print (f"You didn't say the magic word.{counter}")
