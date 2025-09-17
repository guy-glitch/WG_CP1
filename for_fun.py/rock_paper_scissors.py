import random
run = "Y"
play = input("Do you want to play rock paper scissors? Yes or No").strip().lower()
win = 0
tie = 0
lose = 0
while run == "Y":
    if play == "no":
        print("See Ya")
    else:
        com_choice = random.randint(1,3)
        player = input("Rock, Paper, Scissors, Shoot").strip().lower()
        if player == "rock":
            if com_choice == 1:
                print(f"Scissors")
                print("You win")
            if com_choice == 2:
                print(f"Rock")
                print("We tie")
            if com_choice == 3:
                print(f"Paper")
                print("You lose")
            else:
                run = input("Do you want to play again.")
        if player == "Paper":
            if com_choice == 1:
                print(f"Scissors")
                print("You lose")
            if com_choice == 2:
                print(f"Rock")
                print("You win")
            if com_choice == 3:
                print(f"Paper")
                print("We tie")
            else:
                run = input("Do you want to play again.")
        if player == "Scissors":
            if com_choice == 1:
                print(f"Scissors")
                print("We tie")
            if com_choice == 2:
                print(f"Rock")
                print("You lose")
            if com_choice == 3:
                print(f"Paper")
                print("You win")
            else:
                run = input("Do you want to play again.")
                
