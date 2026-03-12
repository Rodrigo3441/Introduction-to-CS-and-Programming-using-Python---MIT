# Problem Set 2, hangman.py
# Name: Rodrigo SG
# Collaborators:
# Time spent: 4 Hours until today
# Started Date: March 11th, 2026
# Finish Date: March 12th, 2026
# Actual Step: 5 out of 5

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    secret_word_length = len(secret_word)
    correct_guesses = 0

    for i in letters_guessed:
        
        if i in secret_word:
            correct_guesses += secret_word.count(i)
    
    if correct_guesses == secret_word_length:
        return True
    else:
        return False                    



def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # apple: input
    # *pp*e: output
    
    # secret_word_length = len(secret_word)
    # output_string = '*' * secret_word_length


    # for i in letters_guessed:
    #     str_position = 0

    #     if i in secret_word:
    #         for j in secret_word:
                
    #             if i == j:
    #                 letter_position = secret_word.find(j, str_position)
    #                 output_string = output_string[:letter_position] + secret_word[letter_position] + output_string[letter_position+1:]
    #                 print(output_string)
    #             str_position += 1
    
    # return output_string

    output = ''

    for letter in secret_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += '*'

    return output


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    letters_available = string.ascii_lowercase
    output = ''
    for letter in letters_available:
        if letter not in letters_guessed:
            output += letter

    return output
    



def separator() -> None:
    """"
    This function prints a separator for better interface on console
    """
    print('--------------')


#def get_user_guess(secret_word: string, with_help: bool, letters_guessed: list) -> tuple[string, bool]:
    

def reveal_letter(secret_word: string, available_letters: string):
    """
        secret_word: the word the computer has chosen for the game
        available_letters: the letters the user has guessed

        this function will reveal a random letter of the secret word
    """

    while True:
        new = random.randint(0, len(available_letters)-1)

        if available_letters[new] in secret_word:
            print(f'Letter revealed: {available_letters[new]}')
            return available_letters[new]


def return_unique_letters(secret_word: string) -> int:
    """
        secret_word: the word the computer has chosen for the game

        this function will count the number of unique letters in the secret_word
        and return an integer number for this count
    """
    passed_letters = []
    total_unique_letters = 0

    for letter in secret_word:
        if letter not in passed_letters:
            passed_letters.append(letter)
            total_unique_letters += 1
    
    return total_unique_letters

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = []
    guesses = 10
    

    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {len(get_word_progress(secret_word, letters_guessed))} letters long')

    while True:
        separator()
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        # guess, correct_guess = get_user_guess(secret_word, with_help, letters_guessed)
        # letters_guessed.append(guess)

        # if not correct_guess:
        #     guesses -= 1

        while True:
            guess = input('Please guess a letter: ').lower().strip()

            """
                About this nested structure:
                if guess: checks if the user entered a guess and not an empty string;

                if guess != '!':
                ----if the game is not being played in with_help mode , and the user enters '!':
                    
                    inside else clause the system will check:
                ----if with_help: 
                --------if guesses > 3:
                ------------only if the game is being played on with_help mode and the user 
                ------------has more than 3 lifes the help can be used
                --------otherwise the help won't be allowed (because one letter reveal costs three lifes)
                ----otherwise without_help mode the system won't allow '!' symbol, only letters
                
                if guess not in letters_guessed: checks if the user has already entered that
                letter, not allowing the same letter again;

                if guess.isalpha() and len(guess) == 1: checks if the user guess only contain
                letters and verifyif the guess is only one letter long 
                
                if guess in secret_word: verify if the user guess is in the secret_word,
                so it checks wether the guess is correct or wrong
            """
            if guess:
                if guess != '!':
                    if guess not in letters_guessed:
                        if guess.isalpha() and len(guess) == 1:
                            if guess in secret_word:
                                letters_guessed.append(guess)
                                print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
                                break

                            else:
                                letters_guessed.append(guess)
                                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
                                
                                if guess in ('a','e','i','o','u'):
                                    guesses -= 2
                                else:
                                    guesses -= 1
                                break
                                
                        else:
                            print(f'Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}')    
                            break
                    else:
                        print(f'Oops! You\'ve already guessed that letter: {get_word_progress(secret_word, letters_guessed)}')
                        break
                else:
                    if with_help:
                        if guesses > 3:
                            help_letter = reveal_letter(secret_word, get_available_letters(letters_guessed))
                            letters_guessed.append(help_letter)
                            guesses -= 3
                            print(get_word_progress(secret_word, letters_guessed))
                            break
                        else:
                            print(f'Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}')
                    else:
                        print('The game help mode is off! Help not allowed.')
            else:
                print('You cannot send an empty guess! Try again.')
            
        if has_player_won(secret_word, letters_guessed):
            total_score = (guesses + 4 * return_unique_letters(secret_word)) + (3 * len(secret_word))
            separator()
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            break
        if guesses <= 0:
            separator()
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

