from random import randint
from art import logo
easy_turns = 10
Hard_turns = 5

#Function to check the users guess.
def check_answer(guess,answer,turns):
  """Checks answer against guess."""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it. The answer was {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == 'easy':
    return easy_turns
  else:
    return Hard_turns

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game.")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  turns = set_difficulty()
  guess  = 0
  while guess != answer:
    print(f"You have {turns} attempts to guess the number.")
    guess = int(input("Make a guess"))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You ran out of guesses you lose.")
      break
    elif guess != answer:
      print("Guess again.")

play_game()