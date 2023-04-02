import random

# Roll two dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Calculate the sum of the two dice rolls
sum = dice1 + dice2

# Check if the sum is even or odd
if sum % 2 == 0:
    result = "even"
else:
    result = "odd"

# Ask the player to guess if the sum is even or odd
guess = input("Guess if the sum of two dice rolls is even or odd: ").lower()

# Check if the player's guess is correct
if guess == result:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, you guessed incorrectly. The total was", sum, "which is", result)
