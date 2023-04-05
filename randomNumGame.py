import random
import time
randNum = random.randint(1,40)
guessRight = 5;
while True:
    userGuess = int(input("Your guess: "))
    if(userGuess < randNum):
        print("Checking...")
        time.sleep(1)
        print("Enter greater number")
        guessRight -= 1
    elif(userGuess > randNum):
        print("Checking...")
        time.sleep(1)
        print("Enter less number")
        guessRight -= 1
    else:
        print("Checking...")
        time.sleep(1)
        print(f"Good job! You find it! The number was {randNum}.")
        break
    if(guessRight == 0):
        print("You have no more right, sorry...")
        break
