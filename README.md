LinkedIn REACH
Mastermind Game
Stefan Daniels

The purpose of this project is to showcase interviewees' coding skills by creating a one player game - Mastermind. The final game file is main.py and the game is to be played from the command line. The game can be started with the command 'python3 main.py.'

To begin, codeGen.py is the api created to obtain random digits from https://www.random.org/. This is used to create the code for the Mastermind game. As an extension to the game, having the ability to adjust the difficulty of the game stems from the two functions in codeGen. Those two methods create two types of codes for the game - digits for the code that will be unique digits (getUniqueCode has no repeat numbers) and random digits (getRandomCode possible repeat numbers). 

The main.py file starts by importing codeGen (to generate the code), re (for regular expressions), and colorama (to map colors to digits (an extension to the game)).

The difficultyLevel function is an extension to the game that takes the user's input after they are given the option to select the game difficulty level. The difficulty levels have two main differences - the number of digits in the code and whether the code is unique or possibly has repeat numbers.

0 - Newb - three unique digits
1 - Easy - four unique digits
2 - Medium - four random digits (possible repeats)
3 - Hard - five random digits (possible repeats)

The codeColor function is an extension to the game that color-codes the digits in the code. The function takes the code obtained through the difficultyLevel and codeGen functions and assigns the colors to respective numbers in the code. The colored digits appear in two locations throughout the game - in the 'Your Guess' column in the player's guess history and at the end when revealing the code. 

The codeString function is used to change the code/data type from an integer to a string. This allows the code to be accessed and displayed (with a space between each codestr) if/when the user requests a hint or wants to view the code.

The validateInput function is used to validate the input the user passes in when playing the game. The user must input digits 0-9 (although the game is 0-7) equal to the length of the code (depending on the difficulty level).

The userInput function is used to take three types of input from the user. The possible inputs during the game are the number guesses where the player tries to guess the code, 'hint' to reveal the first two digits of the code to the player, and 'code' to reveal the code to the player. 

The matchGuess function is used to compare the player's guesses to the code. The parameters code and guess are used to make the comparisons depending on the length of the code and guess. There is a counter to keep track of the correct number (correctNum) and correct location (correctLocation). The digits in the code (codeMarked) and user guess (guessMarked) track the numbers that have been evaluated. Those 'marked' variables adjust according to the possible outcomes of the comparisons (ex. adjusting correctNum in case there are repeat digits). The function displays the number of correct guesses and number of correct locations.

The displayHistory function is used to create a simple interface to display the player's previous guesses and their results by showing their guess number, correct numbers, correct locations, and the respective guess. 

The game function is used to provide the guidelines of the game to the user, obtain the user's name, establish the difficulty level, display the number/color pairs, count and display the remaining guesses, and provide the user with tips on how to play the game, and the results if the player wins or loses. # Mastermind
