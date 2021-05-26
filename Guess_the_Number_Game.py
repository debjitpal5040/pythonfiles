#This is a guess the number game
import random
print("Hello!!! What is your name?")
name = str(input())
print("Hii!!",name + ", I am thinking of a number between 1 to 20")
secretNumber = random.randint(1,21)
for guessesTaken in range(1,6):
   print("Take a guess")
   guess = int(input())
   if guess < secretNumber:
      print("Your guess is low")
   elif guess > secretNumber:
      print("Your guess is high")
   else:
      break  # This Condition is for the correct guess
if guess == secretNumber:
      print("Great! "+ name + " You have guessed my number in " + str(guessesTaken) + " guesses.")
else:
   print("Oops!! The number I was thinking of was " + str(secretNumber))
