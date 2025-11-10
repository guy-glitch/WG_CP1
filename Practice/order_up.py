#WG 1st Order Up
#create a dictionary for each type of menu and putting it into a dictionary called menu
drink = {
    "Coke":30,
    "Water":30,
    "Dr. Pepper":3.99,
    "Sprite":300
}
main_course = {
    "Burger":10.11,
    "Steak":20,
    "Chiken Strip":10.12,
    "Brussel Sprouts":3.99
}
sides = {
    "Fries Small":2,
    "Fries Large":3.99,
    "Salad":3.99,
    "Brussel Sprouts":3.99,
    "Fried Cheese":3.99
}
order = {}
#tell them that this is the menu
print("This is the Menu")
#tell them this is there main course opitons
print("Your main course options are:")
#what tell them there main dish options
for options in main_course:
    print(f"{main_course[options]}")
