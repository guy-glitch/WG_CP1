#WG 1st Order Up
#import random as r for simplicity
import random as r
#create a dictionary for each type of menu and putting it into a dictionary called menu
waiter_limbs = ["head", "torso", "arm", "leg"]
waiter_health = 20
order_limbs = ["head", "torso", "arm", "leg"]
order_health = 10
drink = {
    "Coke":30,
    "Water":30,
    "Dr Pepper":3.99,
    "Sprite":300
}
main_course = {
    "Burger":10.11,
    "Steak":20,
    "Chiken Strip":10.12,
    "Brussel Sprouts Meal":4
}
sides = {
    "Fries Small":2,
    "Fries Large":3.99,
    "Salad":3.99,
    "Brussel Sprouts Side":3.99,
    "Fried Cheese":3.99
}
order = {
    "Your Order":""
}
#loop through until order is posisble
while True:
    #tell them that this is the menu
    print("This is the Menu. I am Your waiter Gaston")
    #tell them this is there main course opitons
    print("Your main course options are:")
    #what tell them there main dish options
    for key, options in main_course.items():
        print(f"{key}:{main_course[key]}")
    #let them choose what choice they want to make
    main_choice = input("What main course do you want?").strip().title()
    #check if the choice is on the menu
    if main_choice in main_course:
        #set the value of their updated order
        #create a item in the order dictionary
        order[main_choice]=main_course[main_choice]
        #end loop
        break
    #tell them that there order doesn't exist
    else:
        print("Incorrect order again")
    
#loop through until the order is correct and works
while True:
    #tell them this is there sides opitons
    print("Your side options are:")
    #what tell them there main dish options
    for key, options in sides.items():
        print(f"{key}:{sides[key]}")
    #let them choose what choice they want to make
    side_choice = input("What first side do you want?").strip().title()
    #check if the choice is on the menu
    if side_choice in sides:
        #set the value of their updated order
        #create a item in the order dictionary
        order[side_choice]=sides[side_choice]
    #tell them that there order doesn't exist
    else:
        print("Incorrect order again")
        #loop through again
        continue
    #let them choose what choice they want to make
    side_choice1 = input("What second side do you want?").strip().title()
    #check if the choice is on the menu
    if side_choice1 in sides:
        #create a item in the order dictionary
        order[side_choice1]=sides[side_choice1]
        #exit the loop
        break
    #tell them that there order doesn't exist
    else:
        print("Incorrect order again")
        #remove the previous item from the order
        order[side_choice]=sides[""]

#loop through until the order is possible
while True:
    #tell them this is there drink opitons
    print("Your drink options are:")
    #what tell them there main dish options
    for key, options in drink.items():
        print(f"{key}:{drink[key]}")
    #let them choose what choice they want to make
    drink_choice = input("What drink do you want?").strip().title()
    #check if the choice is on the menu
    if drink_choice in drink:
        #set the value of their updated order
        #create a item in the order dictionary
        order[drink_choice]=drink[drink_choice]
        #end loop
        break
    #tell them that there order doesn't exist
    else:
        print("Incorrect order again")
#ask them for a tip
tip = float(input("How large of a tip do you want to give? Please input only a number. If you don't want to leave a tip input zero. Thank You"))
#ask them if they want to fight the wiater
fight = input("Do you want to fight your waiter to get free food yes or no")
#if they say yes decide who goes first
if fight == "yes":
    first = r.randint(0,1)
    while waiter_health >0 and order_health >0:
            if first == 0:
                #tell them they get to go first and give give them attack choices
                print("You get to fight first")
                attack_area = input(f"Where do you want to hit the waiter {waiter_limbs[0]}, {waiter_limbs[1]}, {waiter_limbs[2]}, {waiter_limbs[3]}")
                if attack_area == waiter_limbs[0]:
                    attack = input("Do you want to punch or kick.")
                    if attack == "punch":
                        damage = r.randint(1,6)
                        waiter_health -= damage
                    elif attack == "kick":
                        damage = r.randint(1,4)
                        waiter_health -= damage
                    else:
                        print("Invalid input you fail")
                elif attack_area == waiter_limbs(1):
                    attack = input("Do you want to punch or kick.")
                    if attack == "punch":
                        damage = r.randint(1,5)
                        waiter_health -= damage
                    elif attack == "kick":
                        damage = r.randint(1,7)
                        waiter_health -= damage
                    else:
                        print("Invalid input you fail")
                elif attack_area == waiter_limbs(2):
                    attack = input("Do you want to punch or kick.")
                    if attack == "punch":
                        damage = r.randint(1,2)
                        waiter_health -= damage
                    elif attack == "kick":
                        damage = r.randint(1,2)
                        waiter_health -= damage
                    else:
                        print("Invalid input you fail")
                elif attack_area == waiter_limbs(3):
                    attack = input("Do you want to punch or kick.")
                    if attack == "punch":
                        damage = r.randint(1,3)
                        waiter_health -= damage
                    elif attack == "kick":
                        damage = r.randint(1,5)
                        waiter_health -= damage
                    else:
                        print("Invalid input you fail")
                else:
                    print("You aimed at nothing you do no damage.")
                first = 1
            elif first == 1:
                target = r.choice(order_limbs)
                print(f"They attack your {target}")
                attack_type = r.randint(0,1)
                if attack_type == 0:
                    damage = r.randint(1,7)
                    order_health -= damage
                else:
                    damage = r.randint(1,5)
                    order_health
                first = 0
    if waiter_health <= 0:
        print("You won you don't have to pay")
        won = 0
    elif order_health <= 0:
        print("You lost you have to pay double")
        won = 2
#get there total cost
order["total"]=won(main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice]+0.03*(main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice])+tip)
order["total"]=round(order["total"], 2)
#print out the order
for key, options in order.items():
    print(f"{key}:{order[key]}")
print("Thank you for your patronage.")

