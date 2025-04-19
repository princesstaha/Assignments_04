import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Prompt the user for a guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            # Handle non-integer inputs gracefully
            print("That's not a valid number. Please enter an integer.")
            continue

        attempts += 1

        # Check the user's guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

if __name__ == '__main__':
    guess_the_number()