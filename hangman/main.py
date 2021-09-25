# card info from http://mtgjson.com

# init: choose a random card name
from random import randint

with open('CardNames.txt', 'rb') as f:
    allCards = f.read().splitlines()

card = list(allCards[randint(0, len(allCards))].decode('utf-8'))

# keep track of wrong guesses, right guesses, and all guesses separately; all guesses stored as a dictionary makes it easier to check if a letter has previously been guessed
wrongGuesses = []
guessed = {}
correctGuesses = set(''.join(filter(str.isalpha, card)).lower())

# this is an admittedly messy way to conditionally draw parts of the hang(ed)man based on number of wrong guesses
def drawHangman():
    # f-string doesn't allow for backslash, so I assign it as a variable
    backslash = "\\"
    print("  ___ ")
    print(" |   |")
    print(f" |   {'O' if len(wrongGuesses) >= 1 else ' '}")
    print(f" |  {backslash if len(wrongGuesses) >= 2 else ' '}{'|/' if len(wrongGuesses) >= 3 else ' '}")
    print(f" |   {'|' if len(wrongGuesses) >= 4 else ' '}")
    print(f"_|_ {'/' if len(wrongGuesses) >= 5 else ' '} {backslash if len(wrongGuesses) >= 6 else ' '}")

# this checks the user input to see if it's a valid series of new guesses
# accept only alphabetical characters, then check each letter to see if it was guessed
def verifyGuess(inputString, unrevealed):
    if not inputString.isalpha():
        print("Please input only alphabetical characters!")
        return False
    elif len(set(inputString)) != len(inputString):
        print("Please do not enter duplicate letters!")
        return False
    elif len(inputString) > unrevealed:
        print("Too many letters guessed!")
        return False

    newGuesses = list(inputString)
    for letter in newGuesses:
        if guessed.get(letter):
            print("You have entered at least one letter that was previously guessed!")
            return False
    return True

# print the word with letters separated by spaces, replacing each letter that has not been guessed with underscore
def displayWord():
    unrevealed = 0
    for char in card:
        if not char.isalpha() or guessed.get(char.lower()):
            print(char, end=" ")
        elif char.isalpha() and not guessed.get(char.lower()):
            print("_", end=" ")
            unrevealed += 1
    print("")
    return unrevealed

# if a letter in the word has not been guessed, return false, else return true after the entire word is checked and every letter has been guessed
def gameWin():
    if len(correctGuesses) == 0:
        return True
    else:
        return False

# print the word with correctly guessed letters revealed, the hang(ed)man and the wrong guesses so far
def showGameState():
    print("")
    unrevealed = displayWord()
    print("")
    drawHangman()
    print(f"Wrong guesses ({len(wrongGuesses)}/6):")
    print(" ".join(wrongGuesses))
    return unrevealed

# a while loop will run as long as the game has not ended, at the end of each round, will check for game loss or win (mutually exclusive, loss takes precedence)
unrevealed = showGameState()
gameEnd = False

while not gameEnd:
    validInput = False
    
    while not validInput:
        inputString = input("Guess one or more letters (no separators): ").lower()
        validInput = verifyGuess(inputString, unrevealed)
        
    for letter in list(inputString):
        guessed[letter] = True
        if not letter in card and not letter.upper() in card:
            wrongGuesses.append(letter)
        else:
            correctGuesses.remove(letter)
    
    unrevealed = showGameState()
    
    if len(wrongGuesses) >= 6:
        print("You lost!")
        print(f"The card was: {''.join(card)}")
        gameEnd = True
    
    elif gameWin():
        print("You won!")
        gameEnd = True