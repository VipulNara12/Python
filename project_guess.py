# Guess the Number

import random

randomNumber = random.randint(0, 100)
print(randomNumber)
guessNumber = None
guess = 0

while(guessNumber != randomNumber):
    guessNumber = int(input("Guess the Number\n"))
    guess += 1
    if(guessNumber == randomNumber):
        print("You guessed the number right.")
    else:
        if(guessNumber > randomNumber):
            print("You guessed it wrong. Enter the smaller Number.")
        else:
            print("You guessed it wrong. Enter the Greater Number.")

print(f"You guessed the number in {guess} guesses")
