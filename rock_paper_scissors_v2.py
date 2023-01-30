import random

gamelist = ["Rock", "Paper", "Scissors"]

print("Let's play a game")

p_score = 0
cpu_score = 0

rounds = int(input("How many rounds do you play? :"))
round_counter = 0

player_prev = []

def analyze_player_choices(choices):
  rock_count = choices.count("Rock")
  paper_count = choices.count("Paper")
  scissors_count = choices.count("Scissors")
  
  if (rock_count == paper_count) or \
  (rock_count == scissors_count) or \
  (paper_count == scissors_count):
    return random.choice(gamelist)
  elif rock_count > paper_count and rock_count > scissors_count:
    return "Paper"
  elif paper_count > rock_count and paper_count > scissors_count:
    return "Scissors"
  elif scissors_count > rock_count and scissors_count > paper_count:
    return "Rock"
  else:
    return random.choice(gamelist)

while True:

  round_counter += 1
  print(f" Round {round_counter}")

  cpu = random.choice(gamelist)

  while True:
    player = (input("Choose your action 'Rock - Paper - Scissors':").capitalize())
    if player == "Rock":
      break
    elif player == "Paper":
      break
    elif player == "Scissors":
      break
    else:
      print("Please try again.")

  print(f"Player: {player} \t {cpu} :CPU")

  if player_choice in gamelist:
    player_prev.append(player_choice)
    
    computer_choice = analyze_player_choices(player_prev)

  if player == cpu:
    print("It's a tie!")
  elif (player == "Rock" and cpu == "Scissors") or \
    (player == "Paper" and cpu == "Rock") or \
    (player == "Scissors" and cpu == "Paper"):
    print("You win!")
    p_score += 1
  else:
      print("You lose.")
      cpu_score += 1

  if round_counter == rounds:
    print(f"Player {p_score} : {cpu_score} CPU")
    if p_score == cpu_score:
      print("There is no winner, tie.")
    elif p_score > cpu_score:
      print("The winner is Player")
    else:
      print("The winner is CPU")
    again = input("Would you like to play again? (y/n):")
    if again == "n":
      break
    else:
      round_counter = 0
      p_score = 0
      cpu_score = 0
      rounds = int(input("How many rounds do you play? :"))
