#!/usr/bin/env python3
#*******************************************************
#       Filename: ps4c.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Part C: Substitution Cipher
#       Created on: 2018-11-13 15:38:58
#*******************************************************

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        encryption_dict = {}
        # Map the consonants
        consonants = CONSONANTS_LOWER + CONSONANTS_UPPER
        for char in consonants:
            encryption_dict[char] = char

        # Map the lowercase vowels
        for i in range(len(VOWELS_LOWER)):
            encryption_dict[VOWELS_LOWER[i]] = vowels_permutation[i]

        # Map the uppercase vowels
        for i in range(len(VOWELS_UPPER)):
            encryption_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()

        return encryption_dict


    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''
        message_text_encrypted = []
        for char in self.message_text:
            if char.isalpha():
                message_text_encrypted.append(transpose_dict[char])
            else:
                message_text_encrypted.append(char)

        return ''.join(message_text_encrypted)




class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        '''
        result_list = []
        vowels_permutations_list = get_permutations(VOWELS_LOWER)
        # Try every possible permutation
        for elem in vowels_permutations_list:
            count = 0
            enc_dict = self.build_transpose_dict(elem)
            text = self.apply_transpose(enc_dict)
            for word in text.split():
                if is_word(self.valid_words, word):
                    count += 1
            result_list.append((count, text))

        # Find the maximum number of words
        count_max = max([k for (k, v) in result_list ])
        for (k, v) in result_list:
            if k == count_max:
                result = v

        # Return the result
        return result



if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()

    # My Example test case 1
    message_1 = SubMessage("HELLO WORLD!")
    permutation_1 = "eaiuo"
    enc_dict_1 = message_1.build_transpose_dict(permutation_1)
    print("Original message:", message_1.get_message_text(), "Permutation:", permutation_1)
    print("Expected encryption:", "HALLU WURLD!")
    print("Actual encryption:", message_1.apply_transpose(enc_dict_1))
    enc_message_1 = EncryptedSubMessage(message_1.apply_transpose(enc_dict_1))
    print("Decrypted message:", enc_message_1.decrypt_message())
    print()

    # My Example test case 2
    message_2 = SubMessage("Hello, snowball!")
    permutation_2 = "iouea"
    enc_dict_2 = message_2.build_transpose_dict(permutation_2)
    print("Original message:", message_2.get_message_text(), "Permutation:", permutation_2)
    print("Expected encryption:", "Holle, snewbill!")
    print("Actual encryption:", message_2.apply_transpose(enc_dict_2))
    enc_message_2 = EncryptedSubMessage(message_2.apply_transpose(enc_dict_2))
    print("Decrypted message:", enc_message_2.decrypt_message())
    print()



