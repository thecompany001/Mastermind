import codeGen
import re
from colorama import Fore, Back, Style


def difficultyLevel():
    global code
    print("\nGame Difficulty")
    print("0 - Newb \n1 - Easy \n2 - Medium \n3 - Hard")
    userInput = input("\nWhat difficulty? ")
    if userInput.lower() == 'newb' or userInput == '0':
        code = codeGen.getUniqueCode(3, 0, 4, 1, 10, 'plain', 'new')
        return 3
    elif userInput.lower() == 'easy' or userInput == '1':
        code = codeGen.getUniqueCode(4, 0, 7, 1, 10, 'plain', 'new')
        return 4
    elif userInput.lower() == 'medium' or userInput == '2':
        code = codeGen.getRandomCode(4, 0, 7, 1, 10, 'plain', 'new')
        return 4
    elif userInput.lower() == 'hard' or userInput == '3':
        code = codeGen.getRandomCode(5, 0, 7, 1, 10, 'plain', 'new')
        return 5


def codeColor(code):
    colors = {'0': Fore.WHITE, '1': Fore.BLACK, '2': Fore.BLUE, '3': Fore.GREEN,
              '4': Fore.CYAN, '5': Fore.RED, '6': Fore.YELLOW, '7': Fore.MAGENTA}
    for i in code:
        print(colors[i]+i, end=" ")
    print(Style.RESET_ALL, end="")


def codeString(code):
    codestr = ""
    for digit in code:
        codestr += digit + " "
    return codestr


def validateInput(input, length):
    if len(input) == 0:
        return False

    pattern = re.compile("[0-9 ]+")
    if pattern.match(input) == False:
        return False

    numbers = re.split(r'\s+', input)
    if len(numbers) != length:
        return False

    return True


def userInput(length):

    while True:
        print("Please enter numbers in this format: '1 2 3 4' ")
        print("Enter 'hint' to view the first two digits in the code")
        print("Enter 'code' to view the code\n")
        guess = input("Enter your guess: ")

        if guess.lower() == "hint":
            print("\nHint: ", codeString(code[0]), codeString(code[1]), "\n")

        elif guess.lower() == "code":
            print("\nCode: ", codeString(code), "\n")

        elif validateInput(guess, length) == True:
            return guess

        else:
            print(f"Please guess {length} digits")


def matchGuess(code, guess, length):
    correctNum = 0
    correctLocation = 0
    codeMarked = ["NOMATCH"]*length
    guessMarked = ["NOMATCH"]*length

    for i in range(len(guess)):
        for j in range(len(code)):
            if guess[i] == code[j] and i == j:

                if codeMarked[i] != "CORRECTLOCATION":
                    codeMarked[j] = "CORRECTLOCATION"
                    guessMarked[j] = "CORRECTLOCATION"
                    correctLocation += 1
                    correctNum += 1

                if codeMarked[j] == "CORRECTNUMBER":
                    correctNum -= 1

                if guessMarked[i] == "CORRECTNUMBER":
                    correctNum -= 1

            elif guess[i] == code[j] and i != j and guessMarked[i] == "NOMATCH":

                if codeMarked[j] == "NOMATCH":
                    guessMarked[i] = "CORRECTNUMBER"
                    codeMarked[j] = "CORRECTNUMBER"
                    correctNum += 1

    print(str(correctNum) + " Correct number(s) and " +
          str(correctLocation) + " correct location(s) ")

    return correctNum, correctLocation


def displayHistory(history):
    print(f"{'*'*85:<85}")
    print(f"{'Guess Number':<25}{'Correct Numbers':<25}{'Correct Locations':<25}{'Your Guess':<25}")

    for index in range(len(history)):
        print(f"{index+1:<25}{history[index][0]:<25}{history[index][1]:<25}", end="")
        codeColor(history[index][2])
        print()
    print(f"{'*'*85:<85}")


def game():
    print(Style.RESET_ALL, end="")
    print("------------------------------------")
    print("\t    MASTERMIND")
    print("------------------------------------")

    colors = {"White", "Magenta", "Red", "Green",
              "Yellow", "Blue", "Black", "Cyan"}

    print("------------------------------------")
    print("\t       MENU")
    print("------------------------------------")

    name = input("What is your name? ")

    length = difficultyLevel()

    print("\nEnter the code using numbers")
    print("0 - White 1 - Black 2 - Blue 3 - Green\n4 - Cyan 5 - Red 6 - Yellow 7 - Magenta")
    print("For Example: Black Red Blue Yellow ---> 1 5 2 6")
    print("------------------------------------")
    guessCount = 0
    history = list()

    while True:
        if guessCount >= 10:
            print("That was 10 guesses. You lose!!")
            break

        print(f'You have {10-guessCount} remaining guesses\n')
        inputStr = userInput(length)
        guessCount += 1
        guess = re.split(r'\s+', inputStr)

        correctNumbers, correctLocations = matchGuess(code, guess, length)

        guessResults = [correctNumbers, correctLocations, guess]
        history.append(guessResults)
        displayHistory(history)

        if correctLocations == length:
            print(f'\n~*~ Congratulations {name}, you won! ~*~\n')
            break

    print("Correct Code: ", end="")
    codeColor(code)
    print("\n")
    print("Thanks for playing.\n")


game()