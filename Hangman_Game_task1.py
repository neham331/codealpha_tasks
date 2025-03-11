import random

def choose_word():
    words = ["python", "programming", "hangman", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").strip().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            incorrect_guesses += 1
            print(f"Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")
        else:
            print("Good job! That letter is in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The correct word was:", word)

if __name__ == "__main__":
    hangman()