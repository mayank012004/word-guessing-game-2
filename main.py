import random

# List of words
WORDS = ("follow", "waking", "insane", "chilly", "massive", "ancient", "zebra", "logical", "never", "nice")

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game(player_name):
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_remaining = 6
    print(f"\n{player_name}, it's your turn!")

    while attempts_remaining > 0:
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            attempts_remaining -= 1
            print(f"Incorrect! You have {attempts_remaining} attempts left.")

        if set(word_to_guess) <= guessed_letters:
            print(f"Congratulations {player_name}! You guessed the word: {word_to_guess}")
            return attempts_remaining

    print(f"Sorry {player_name}, you didn't guess the word. It was: {word_to_guess}")
    return 0

def main():
    print("Welcome to the Word Guessing Game!")
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    player1_score = play_game(player1_name)
    player2_score = play_game(player2_name)

    print("\nGame Over! Here's the scoreboard:")
    print(f"{player1_name}: {player1_score} points")
    print(f"{player2_name}: {player2_score} points")

    if player1_score > player2_score:
        print(f"Congratulations {player1_name}! You won the game!")
    elif player2_score > player1_score:
        print(f"Congratulations {player2_name}! You won the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
