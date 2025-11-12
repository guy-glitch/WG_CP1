#WG 1st Order Up
#import random as r for simplicity
import random as r
#create a dictionary for each type of menu and putting it into a dictionary called menu
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
waiter = r.randint(1,3)

if waiter == 1:
    #loop through until order is posisble
    while True:
        #tell them that this is the menu
        print("This is the Menu")
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
    tip = float(input("How large of a tip do you want to give? Please input only a number. If you don't want to leave a tip input zero. Thank You"))

    #get there total cost
    order["total"]=main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice]+0.03*(main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice])+tip
    order["total"]=round(order["total"], 2)
    #print out the order
    for key, options in order.items():
        print(f"{key}:{order[key]}")
    print("Thank you for your patronage.")


elif waiter == 2:
    #loop through until order is posisble
    while True:
        #tell them that this is the menu
        print("This is the Menu")
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
    tip = float(input("How large of a tip do you want to give? Please input only a number. If you don't want to leave a tip input zero. Thank You"))

    #get there total cost
    order["total"]=main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice]+0.03*(main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice])+tip
    order["total"]=round(order["total"], 2)
    #print out the order
    for key, options in order.items():
        print(f"{key}:{order[key]}")
    print("Thank you for your patronage.")

else:
    #loop through until order is posisble
    while True:
        #tell them that this is the menu
        print("This is the Menu")
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
            print("Incorrect, order again")
    tip = float(input("How large of a tip do you want to give? Please input only a number. If you don't want to leave a tip input zero. Thank You"))

    #get there total cost
    order["total"]=main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice]+0.03*(main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice])+tip
    order["total"]=round(order["total"], 2)
    #print out the order
    for key, options in order.items():
        print(f"{key}:{order[key]}")
    print("Thank you for your patronage.")