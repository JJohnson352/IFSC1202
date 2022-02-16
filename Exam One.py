N = input("Hello! What's your Name? ")
print( N, "I am thinking of a number between 1 and 20.")
print("You have 5 guesses")
from random import randint
X = randint(1, 20)
for i in range(1,5+1):
    a = int(input("Enter Your Guess Here: "))
    if a > X:
         print("guess too high")
    if a < X:
        print("guess too low")
    if a == X:
        print("Good Job", N, "You Guessed my number in "+str(i)+" guesses")
if X is not a:
    print("Nope. The number I was thinking of was") 
    (print(X))