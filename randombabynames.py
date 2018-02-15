import string
import random

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_letters

letter1 = input("input 'c' for consonant, 'v' for vowel and 'l' for letters: ")
letter2 = input("input 'c' for consonant, 'v' for vowel and 'l' for letters: ")
letter3 = input("input 'c' for consonant, 'v' for vowel and 'l' for letters: ")
letter4 = input("input 'c' for consonant, 'v' for vowel and 'l' for letters: ")

def generator():
    if letter1 == 'c':
        new_letter1 = random.choice(consonants)
    elif letter1 == 'v':
        new_letter1 = random.choice(vowels)
    elif letter1 == 'l':
        new_letter1 = random.choice(letter)
    else: 
        return "You didnt enter the appropriate one.. Try again later"
    
    if letter2 == 'c':
        new_letter2 = random.choice(consonants)
    elif letter2 == 'v':
        new_letter2 = random.choice(vowels)
    elif letter2 == 'l':
        new_letter2 = random.choice(letter)
    else: 
        return "You didnt enter the appropriate one.. Try again later"
    
    if letter3 == 'c':
        new_letter3 = random.choice(consonants)
    elif letter3 == 'v':
        new_letter3 = random.choice(vowels)
    elif letter3 == 'l':
        new_letter3 = random.choice(letter)
    else: 
        return "You didnt enter the appropriate one.. Try again later"
   
    if letter4 == 'c':
        new_letter4 = random.choice(consonants)
    elif letter4 == 'v':
        new_letter4 = random.choice(vowels)
    elif letter4 == 'l':
        new_letter4 = random.choice(letter)
    else: 
        return "You didnt enter the appropriate one.. Try again later"

    final_letters = new_letter1+new_letter2+new_letter3+new_letter4
    return final_letters 

for i in range(5):
    print(generator())
