#WG 1st Order Up
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
#tell them that there order doesn't exist
else:
    print("Incorrect order again")


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
#let them choose what choice they want to make
side_choice1 = input("What second side do you want?").strip().title()
#check if the choice is on the menu
if side_choice1 in sides:
    #create a item in the order dictionary
    order[side_choice1]=sides[side_choice1]
#tell them that there order doesn't exist
else:
    print("Incorrect order again")



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
#tell them that there order doesn't exist
else:
    print("Incorrect order again")


#get there total cost
order["total"]=main_course[main_choice]+sides[side_choice]+sides[side_choice1]+drink[drink_choice]
#print out the order
for key, options in order.items():
    print(f"{key}:{order[key]}")