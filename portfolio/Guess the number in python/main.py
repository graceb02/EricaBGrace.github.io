#Number Guessing Game

#ascii art import
from art import logo
print(logo)

from random import randint
#global variables
game_over = False

#game play
#welcome statement and setting the secret number
print("Welcome to Guess The Number!")
print("I am thinking of a number between 1 and 100.")
the_number = randint(1, 100)

#determine number of tries
difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
print(difficulty)
if difficulty == 'hard':
  tries = 5
elif difficulty == 'easy':
  tries = 10
else:
  print("Invalid response. Game over.")
  game_over = True

#while loop for guessing while there are tries left and user has not won
while not game_over and tries >= 1:
  #if block to address grammar changes when it gets to one turn
  if tries > 1:
    print(f"You have {tries} attempts remaining to guess the number.")
  elif tries == 1:
    print("You have 1 attempt remaining to guess the number.") 
  
  # user makes their guess for each try and tries counter decreases
  guess = int(input("Make a guess: "))
  tries -= 1
  
  # checking user's guess against the secret number
  # if block - more than one try left
  if tries != 0:
    if guess > the_number:
      print("Too high. Guess again.")
    elif guess < the_number:
      print("Too low. Guess again.")
    else:
      print(f"You got it! The number was {the_number}!")
      game_over = True
  # else block - user is on last try
  else:
    if guess != the_number:
      print(f"That was your last guess. You lose. The number was {the_number}")
    else:
      print(f"You got it! The number was {the_number}!")
    game_over = True    
