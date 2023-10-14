import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' or ' ' in word:
        word = random.choice(word)
    return word



    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
                    
    elif user_letter in used_letters:
        print('You already used that letter, Try again.')
                    
    else:
        print('invalid character try again')             

