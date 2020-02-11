# Hangman game
# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable
# in a loop, do the following
# display the hangman using the gallows

# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won
import random
# ask if they want to play again
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

print(gallows[0])



alphabet = [chr(x) for x in range(65, 65 + 26)]
print(alphabet)

random.shuffle(alphabet)
print(alphabet)

import random
done = False
word_list =["Meerkat","Lion","Squirrel","Snow Leopard","Dog","Red Panda","Raccoon","Tiger","Monkey","Wolf","Cat","Eagle","Owl","Butterfly","Polar Bear","Kookaburra","Hamster","Bird","Guinea Pig","Tortoise","Alligator","Stork","Egret","Sea Lion","Rabbit","Turtle","Ibis","Finch","Panther","Penguin","Dinosaur","Deer","Sheep","Shrimp","Lobster","Starfish"]
choose_word = word_list.pop(random.randrange(len(word_list))).upper()
print(choose_word)
letters_used = []
letters_misses = []
letters_gotten = []

print("Hello and Welcome to hang man! This version is Animal based. Have fun")
while not done:
    guess = input("Choose a letter: ")
    print("The letters you have used are", letters_used)
    print("You have", 6 - len(letters_misses), "lives left")
    for letter in choose_word:
        if guess.upper() == letter in choose_word:
            letters_gotten.append(guess.upper())
            letters_used.append(guess.upper())
            print(letter, end=" ")
        else:
            letters_used.append(guess.upper())
            letters_misses.append(guess.upper())
            print("_", end=" ")















