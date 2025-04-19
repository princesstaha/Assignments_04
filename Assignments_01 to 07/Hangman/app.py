import random

# Word list
word_list = ["python", "streamlit", "hangman", "developer", "interactive"]
word = random.choice(word_list).lower()
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print(f"Game over! The word was: {word}")