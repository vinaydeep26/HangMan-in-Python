
import random
import time

#initialize
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
print("The game is starting!\n Let's play Hangman!")
time.sleep(2)


# The parameters we require to execute the game:
def main():
    global count_of_guesses
    global displayedword
    global word_to_be_guessed
    global already_guessed_list_of_words
    global length
    global choice_to_continue_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"," live","spurious","squeak","sniff","juvenile"
                   ,"mine","allow","mice","educated","pretty","obtainable"]
    word_to_be_guessed = random.choice(words_to_guess)
    length = len(word_to_be_guessed)
    count_of_guesses = 0
    displayedword = '_' * length
    already_guessed_list_of_words = []
    choice_to_continue_game = ""

# A loop to re-execute the game when the first round ends:

def play_loop():
    global choice_to_continue_game
    choice_to_continue_game = input("Do You want to play again? y = yes, n = no \n")
    while choice_to_continue_game not in ["y", "n","Y","N"]:
        choice_to_continue_game = input("Dude? y = yes, n = no \n")
    if choice_to_continue_game == "y":
        main()
    elif choice_to_continue_game == "n":
        print("Yooo we Running")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count_of_guesses
    global displayedword
    global word_to_be_guessed
    global already_guessed_list_of_words
    global choice_to_continue_game
    limit = 5
    guess = input("This is the Hangman Word: " + displayedword + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word_to_be_guessed:
        already_guessed_list_of_words.extend([guess])
        index = word_to_be_guessed.find(guess)
        word_to_be_guessed = word_to_be_guessed[:index] + "_" + word_to_be_guessed[index + 1:]
        displayedword = displayedword[:index] + guess + displayedword[index + 1:]
        print(displayedword + "\n")

    elif guess in already_guessed_list_of_words:
        print("Try another letter.\n")

    else:
        count_of_guesses += 1

        if count_of_guesses == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count_of_guesses) + " guesses remaining\n")

        elif count_of_guesses == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count_of_guesses) + " guesses remaining\n")

        elif count_of_guesses == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count_of_guesses) + " guesses remaining\n")

        elif count_of_guesses == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count_of_guesses) + " last guess remaining\n")

        elif count_of_guesses == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word_to_be_guessed was:",already_guessed_list_of_words,word_to_be_guessed)
            play_loop()

    if word_to_be_guessed == '_' * length:
        print("Congrats! You have guessed the word_to_be_guessed correctly!")
        play_loop()

    elif count_of_guesses != limit:
        hangman()


main()


hangman()