
import random

print("===== NUMBER GUESSING GAME =====")

while True:
    secret_number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Congratulations! You guessed it!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing,  Bye..")
        break
