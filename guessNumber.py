import random
import time

number = random.randint(1, 100)

def intro():
    print("What is your Name?: ")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 ans 200")
    time.sleep(.5)
    print("Go ahead. Guess!!")

def pick():
    guessesTaken = 0
    while guessesTaken < 10:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess <= 100 and guess >= 1:
                guessesTaken = guessesTaken+1
                if guessesTaken < 10:
                    if guess < number:
                        print("The number you guessed is to low ")
                    if guess > number:
                        print("The number you guessed is to high ")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                     break
            if guess > 100 or guess < 1:
                print("The Number isnt in the range")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I dont think that "+enter+" is a number. Sorry")
    
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! you gussed my number in ' +guessesTaken+ 'gusses!')
    
    if guess != number:
        print('Nope. The number I was Thinking was ' +str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes" or playagain == "Y":
    intro()
    pick()
    print("do you want to play again?")
    playagain = input()
