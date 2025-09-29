import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #converting it to a float so the greater then works this is a runtime error
        guess = float(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            #Increase the attempts taken by 1 so that it ends. This is a logical error.
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")
            attempts += 1  
        #The continue was redundant This is a logical error.
        #There wasn't an else to catch everything that failed. This is a logical error
        else:
            print("Incorrect input try again")
    print("Game Over. Thanks for playing!")
start_game()