#This is a guess the number game
import random 
secretNumber = random.randint(1,20)
print("I am thinking of a Number between 1 to 20. ")

#Ask the player to guess 6 times.

for guessTaken in range(1,7):
    print("Take a guess : ")
    guess = int(input())
    if  guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
    if guess == secretNumber:
        print("Congratulations! You got it right in "+str(guessTaken)+"guesses!")
    else:
        print("Nope. The number i was thinking of was "+str(secretNumber))