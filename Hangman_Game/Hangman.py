import random
from Word_list import word_list
from Hangman_art import logo

Go_again = True
while Go_again:
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(logo)

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

                Replay = input("Will you like to play again ? 'y' for yes and 'n' for no: ")
                if Replay == "y":
                    Go_again = True
                else:
                    Go_again = False

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        from Hangman_art import stages

        print(stages[lives])

