#print("hi")

import random

def number_matching_game():
    # Generate a random number between 1 and 100
    match_number = random.randint(1, 100)
    
    # Set the number of guesses to 0
    number_of_guesses = 0
    
    # Ask the player to match the number to the random number
    while True:
        match_guess = input("Match the number to the random number: ")
        number_of_guesses += 1
        
        # Check if the guess is correct
        if int(match_guess) == match_number:
            print("Congs! You matched the number in",number_of_guesses, "guesses.")
            break
        
        # Check if the guess is too high or too low
        elif int(match_guess) < match_number:
            print("Too low! Match again.")
        else:
            print("Too high! Match again.")

# Call the function to start the game.
number_matching_game()

