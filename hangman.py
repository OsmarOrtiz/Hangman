import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' or ' ' in word:
        word = random.choice(word)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   #asigna la cant de palabras en un set    
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #user imput
    while len(word_letters) > 0:
        # letras usadas
        print ('You have used this letters', ' '.join(used_letters))

        #shows only the guessed words
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
            
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print('You already used that letter, Try again.')
        
        else:
            print('invalid character try again')             