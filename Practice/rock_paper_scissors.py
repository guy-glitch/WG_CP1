import random
run = "Y"
play = input("Do you want to play rock paper scissors? Yes or No ").strip().lower()
win = 0
tie = 0
lose = 0
while run == "Y":
    if play == "no":
        print("See Ya")
        run = "N"
    elif play == "yes":
        com_choice = random.randint(1,3)
        player = input("Rock, Paper, Scissors, Shoot ").strip().lower()
        if player == "rock":
            if com_choice == 1:
                print(f"Scissors")
                print("You win")
                win += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again.").strip().lower()
            elif com_choice == 2:
                print(f"Rock")
                print("We tie")
                tie += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
            else:
                print(f"Paper")
                print("You lose")
                lose += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
        elif player == "paper":
            if com_choice == 1:
                print(f"Scissors")
                print("You lose")
                lose += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
            elif com_choice == 2:
                print(f"Rock")
                print("You win")
                win += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again.").strip().lower()
            else:
                print(f"Paper")
                print("We tie")
                tie += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
        elif player == "scissors":
            if com_choice == 1:
                print(f"Scissors")
                print("We tie")
                tie += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
            elif com_choice == 2:
                print(f"Rock")
                print("You lose")
                lose += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again. ").strip().lower()
            else:
                print(f"Paper")
                print("You win")
                win += 1
                print(f"Wins: {win}, Ties: {tie}, Loses: {lose}")
                run = input("Do you want to play again.").strip().lower()

        else:
            print("Incorect input please try again")
            play = input("Do you want to play again.")
    else:
            print("Incorect input please try again")
            play = input("Do you want to play again.")
