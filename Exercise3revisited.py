'''
Write a Python script that implements the "Guess the Number" game.
The script will generate of a random integral number (use the module random) 
from 1 to 100, and ask you to guess it.
The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.

'''

import random


    
secret=random.randint(1,100)

maxNbOfTest=6
currentNbOfTest=1

while currentNbOfTest <= maxNbOfTest:
    
    #resp=input(f"Enter an int in the range [1,100]  {currentNbOfTest}/{maxNbOfTest}: ")
    resp=input("Enter an int in the range [1,100]  "+str(currentNbOfTest)+"/"+str(maxNbOfTest)+": ")
    resp=int(resp)
    
    currentNbOfTest = currentNbOfTest + 1
    if resp < secret:
        print ("Too small !")
    elif resp > secret:
        print ("Too big !")
    else:
        print ("Bingo !") 
        break
else:
    print ("Sorry, the secret number was: ", secret)

    