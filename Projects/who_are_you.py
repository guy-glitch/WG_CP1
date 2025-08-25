import sys
run = input("Would you like to run y/n")
while run == "y":
    name = input("What is your name")
    age =  input("How old are you")
    color = input("What is your favorite color")
    print(f"So your name is {name}, you are {age} years old, and your favorite color is {color}")
    run = input("Would you like to run again y/n")
if run == "n":
    print("Terminating code")
    sys.exit

