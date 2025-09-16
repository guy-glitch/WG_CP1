import random
run = "Y"
play = input("Do you want to play rock paper scissors? Yes or No").strip().lower()

while run == "Y":
    if play == "no":
        print("See Ya")
    else:
        com_choice = random.randomint(1,3)
        player = input("Rock, Paper, Scissors, Shoot").strip().lower()
        if player == "rock":
            if com_choice == 1:
                print(f"Scissors")
                print("You win")
            if com_choice == 1:
                print(f"Rock")
                print("We tie")
            if com_choice == 1:
                print(f"Paper")
                print("You lose")
        if player == "Paper":
            if com_choice == 1:
                print(f"Scissors")
                print("You lose")
            if com_choice == 1:
                print(f"Rock")
                print("You win")
            if com_choice == 1:
                print(f"Paper")
                print("We tie")
                
