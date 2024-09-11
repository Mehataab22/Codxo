"""This Number Guessing Game is an interactive challenge where players try to guess a randomly generated number within a specified range. 
The game begins by asking the player to input the lower and upper bounds for the number range. 
After setting the range, the player has a limited number of guesses, calculated based on the size of the range.
With each guess, the game provides feedback on whether the guess is too high or too low and informs the player of the remaining chances.
If the player guesses correctly, they win; otherwise, they are revealed the correct number at the end"""


import random
import math

def cryptic_challenge():
    print("Welcome to the Cryptic Challenge!")

    # Setting the difficulty levels
    difficulty_levels = {
        " easy": (1, 5),
        "medium": (1, 10),
        "hard": (1, 15)
    }

    # Choosing the difficulty level
    while True:
        difficulty = input("Choose your difficulty level (easy, medium, hard): ")
        if difficulty in difficulty_levels:
            lower, upper = difficulty_levels[difficulty]
            break
        else:
            print("Invalid difficulty level. Please try again.")

    # Generating a random number between lower and upper
    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log2(upper - lower + 1))
    print(f"\nYou've only {total_chances} chances to crack the code!\n")

    # Initializing the number of guesses
    count = 0
    cracked_code = False

    # Guessing loop
    while count < total_chances:
        count += 1
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

        if guess == x:
            print(f"Congratulations! You cracked the code in {count} attempts.")
            cracked_code = True
            break
        elif guess < x:
            print("You're getting warmer, but your guess is too low!")
        else:
            print("You're getting warmer, but your guess is too high!")

        remaining_chances = total_chances - count
        if remaining_chances > 0:
            print(f"You have {remaining_chances} {'chance' if remaining_chances == 1 else 'chances'} left.")
        else:
            print("No chances left!")

    if not cracked_code:
        print(f"\nThe code was {x}. Better luck next time!")

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        cryptic_challenge()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    cryptic_challenge()
