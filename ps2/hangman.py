#!/usr/bin/env python3
#*******************************************************
#       Filename: hangman.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Solution to Problem Set 2
#       Created on: 2018-10-20 17:46:20
#*******************************************************

# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output_word = ''
    for char in secret_word:
        if char not in letters_guessed:
            output_word += '_ '
        else:
            output_word += char
    return output_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output_word = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            output_word += char
    return output_word



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Initialize some parameters
    guesses_remaining = 6
    warnings_remaining = 3
    total_score = 0
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(warnings_remaining))


    while True:
        print("------------")
        # If guesses remaining is less than zero, you fail the game
        if guesses_remaining < 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break
        # If guesses remaining is greater equal than zero, go on the game
        else:
            print("You have {} guesses left.".format(guesses_remaining))
            print("Available letters: {}".format(get_available_letters(letters_guessed)))
            input_letter = input("Please guess a letter: ").lower()
            # Judge whether the input letter is alpha
            if input_letter.isalpha():
                if input_letter in letters_guessed:
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! You've already guessed that letter.You now have {} warnings left: \n{}".format(warnings_remaining, output))
                    else:
                        warnings_remaining = 0
                        guesses_remaining -= 1
                        print("Oops! You've already guessed that letter.You now have no warnings left so you lose one guess: \n{}".format(output))
                else:
                    letters_guessed.append(input_letter)
                    output = get_guessed_word(secret_word, letters_guessed)
                    if input_letter in secret_word:
                        print("Good guess: {}".format(output))
                        if is_word_guessed(secret_word, letters_guessed):
                            total_score = guesses_remaining * len(set(secret_word))
                            print("-------------")
                            print("Congratulation, you won!\nYour total score for this game is: {}".format(total_score))
                            break
                    else:
                        if input_letter in vowels:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
                        print("Oops! That letter is not in my word: {}".format(output))
            # When the input letter is not an alpha characther
            else:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings_remaining, output))
                else:
                    warnings_remaining = 0
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left: {}".format(output))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # strip() can only eliminate the space at the beginning and end of a string.
    # So I use replace() instead.
    my_word_strip = my_word.replace(' ', '')
    if len(my_word_strip) == len(other_word):
        for i in range(len(my_word_strip)):
            # When the character in my_word_strip is not '_' and different from
            # the character in other_word, return false.
            if my_word_strip[i] != '_' and my_word_strip[i] != other_word[i]:
                return False
            # When the character in my_word_strip is '_' but the character has
            # occured in the string, return false
            elif my_word_strip[i] == '_' and other_word[i] in my_word_strip:
                return False
            # Go on the loop
            else:
                continue
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_strip = my_word.replace(' ', '')
    match_words = []
    # Use match_with_gaps func to judge whether word in
    # wordlist matches with my_word.
    for word in wordlist:
        if match_with_gaps(my_word_strip, word):
            match_words.append(word)
        else:
            continue

    # Judge whether match_words is empty
    if len(match_words) == 0:
        print("No matches found")
    else:
        print(' '.join(match_words))




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Initialize some parameters
    guesses_remaining = 6
    warnings_remaining = 3
    total_score = 0
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(warnings_remaining))


    while True:
        print("------------")
        # If guesses remaining is less than zero, you fail the game
        if guesses_remaining < 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break
        # If guesses remaining is greater equal than zero, go on the game
        else:
            print("You have {} guesses left.".format(guesses_remaining))
            print("Available letters: {}".format(get_available_letters(letters_guessed)))
            input_letter = input("Please guess a letter: ").lower()
            # Judge whether the input letter is alpha
            if input_letter.isalpha():
                if input_letter in letters_guessed:
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! You've already guessed that letter.You now have {} warnings left: \n{}".format(warnings_remaining, output))
                    else:
                        warnings_remaining = 0
                        guesses_remaining -= 1
                        print("Oops! You've already guessed that letter.You now have no warnings left so you lose one guess: \n{}".format(output))
                else:
                    letters_guessed.append(input_letter)
                    output = get_guessed_word(secret_word, letters_guessed)
                    if input_letter in secret_word:
                        print("Good guess: {}".format(output))
                        if is_word_guessed(secret_word, letters_guessed):
                            total_score = guesses_remaining * len(set(secret_word))
                            print("-------------")
                            print("Congratulation, you won!\nYour total score for this game is: {}".format(total_score))
                            break
                    else:
                        if input_letter in vowels:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
                        print("Oops! That letter is not in my word: {}".format(output))
            # When the input letter is not an alpha characther
            else:
                # When the input letter is '*', show the hints
                if input_letter == '*':
                    show_possible_matches(output)
                else:
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings_remaining, output))
                    else:
                        warnings_remaining = 0
                        guesses_remaining -= 1
                        print("Oops! That is not a valid letter. You have no warnings left: {}".format(output))





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # Test case
    #secret_word = 'tact'

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
