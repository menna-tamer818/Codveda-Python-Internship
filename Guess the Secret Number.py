import random

# The secret number our game will use (Now it's random!)
secret_number = random.randint(1, 10)

print("--- Guess the Secret Number! ---")
print("I'm thinking of a number between 1 and 10...")

# This is our main game loop
while True:
    try:
        # Get the user's guess. Remember to cast to int!
        guess = int(input("Your guess: "))

        # Check if the guess is correct
        if guess == secret_number:
            print(f"You got it! The number was {secret_number}.")
            print("--- YOU WIN! ---")
            break # Stop the loop because they won
        
        # Give a hint if the guess is wrong
        elif guess < secret_number:
            print("Nope, higher! Try again!")
        else:
            print("Nope, lower! Try again!")

    except ValueError:
        # Handle the error if the user enters something that is not a number
        print("Please enter a valid number!")

print("Game Over. Thanks for playing!")