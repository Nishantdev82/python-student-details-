

import random

print("===== NUMBER GUESSING GAME =====")

while True:
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10!")
            continue

        attempts += 1

        if guess == secret_number:
            print("Congratulations.. You guessed it..")
            print("Attempts:", attempts)
            break
        elif guess < secret_number:
            print("Too low.. Try again.")
        else:
            print("Too high.. Try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing.. Bye...")
        break
