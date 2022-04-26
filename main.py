import random
number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
  guess_limit = 10
elif level == 'hard':
  guess_limit = 5
else:
  print("Please enter a valid difficulty.")
guess_time = 0
end_game = False
while guess_time<guess_limit and not end_game:
  print(f"You have {guess_limit-guess_time} attemps remaining to guess the number.")
  guess_number = int(input("Make a guess: "))
  if guess_number > number:
    print("Too high.")
  elif guess_number < number:
    print("Yoo low.")
  else:
    print(f"You got it! The answer was {guess_number}")
    end_game = True
  guess_time += 1
