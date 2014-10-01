# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # set variables true and false equal to zero
    true = 0
    false = 0
    
    # iterate through the chars in secretWord
    for char in secretWord:
        
        # if the char is in lettersGuessed, increase true by 1
        if char in lettersGuessed:
            true += 1
        
        # if the char is not in lettersGuessed, increase false by 1
        else:
            false +=1
            
    # if false is zero, return True
    if false == 0:
        return True
    
    # otherwise, return False
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # create list for the answer
    answer = [ ]
    
    # iterate through chars in secretWord
    for char in secretWord:
        
        # if the char is in lettersGuessed, append that char to the answer list
        if char in lettersGuessed:
            answer.append(char + ' ')
        
        # otherwise, just append a blank dash placeholder
        else:
            answer.append('_ ')
            
    # return the answer as a string, showing the letters guessed and underscores for the letters not yet guessed
    return ' '.join(answer)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # create a list for the alphabet (alpha)
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # remove values in lettersGuessed from alpha when they have been guessed
    for value in lettersGuessed:
        alpha.remove(value)
    
    # return an updated list alpha showing what letters have not yet been guessed
    return ' '.join(alpha)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # set guessLeft to 8 (the number of guesses the player gets)
    guessLeft = 8
    
    # create a list to store lettersGuessed
    lettersGuessed = [ ]
    
    # find the length of the secretWord
    k = len(secretWord)
    
    # print intro text, tell user the word length
    print str('Welcome to the game, Hangman!')
    print str('I am thinking of a word that is ' + str(k) + ' letters long.')
    print str('-------------')
    
    # while guessLeft is greater than zero (while user still has guesses left)
    while guessLeft > 0:
        
        # print how many guesses are left
        print str('You have ' + str(guessLeft) + ' guesses left.')
        
        # print available letters
        print str('Available letters: ') + getAvailableLetters(lettersGuessed)
        
        # prompt user to guess a letter
        guess = raw_input('Please guess a letter: ')
        
        # make sure letter entered is lowercase
        guessLower = guess.lower()
        
        # add the entered letter to lettersGuessed
        lettersGuessed.append(guessLower)
        
        # if the letter guessed is already in lettersGuessed, print Oops message and show progress using getGuessedWord function
        if lettersGuessed.count(guessLower) > 1:
            print str("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
        
        # if the letter guessed is in secretWord, show progress (including the guess) using getGuessedWord function
        elif guessLower in secretWord:
            print str('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
            
            # if they've guessed the entire word, print Congrats message and break out of the loop
            if isWordGuessed(secretWord, lettersGuessed) == True:
                return str('Congratulations, you won!')
                break
        # otherwise, if letter not in secretWord, decrement guessLeft by 1 and show progress using getGuessedWord function
        else:
            guessLeft -= 1
            print str('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
    # if guessLeft is not >0, tell the user they ran out of guesses and print the secretWord
    else:
        return str('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
