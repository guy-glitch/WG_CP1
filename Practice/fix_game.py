#WG 1st Fix Code
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #This was a string that was trying to have math be done with it so I converted it to a float, added .strip to solve any spaces added before the answer is typed. The first error is a 
        guess = float(input("Enter your guess: ").strip())
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        #Changed to an elif so it worked correctly logical error
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            #Attempts were not changeing so the code repeated forever this is a logical error
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        #not compensating for invalid inputs added else statement this is a Runetime error
        else:
            print("Incorrect input, please enter a number")
        continue
    print("Game Over. Thanks for playing!")
start_game()