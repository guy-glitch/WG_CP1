#WG 1st Shopping List Manager
shopping = []
while True:
    action = input("To add an item to your list type add, to remove an item type remove, to see your list type see, to finish type exit.\n").strip()
    if action == "add":
        add = input("What do you want to add to the list.\n").strip()
        if add in shopping:
            print("Item already in list")
            print(shopping)
        else:
            shopping.append(add)
            print("Item added to the list")
    elif action == "remove":
            print(shopping)
            remove = input("What item would you like to remove\n")
            if remove in shopping:
                shopping.remove(remove)
                print("Item has been removed")
            else:
                print("Please try again item not in list")
    elif action == "see":
        print(shopping)
    elif action == "exit":
        break
    else:
        print("Incorrect input try again")