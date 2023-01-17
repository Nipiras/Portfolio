import random

gamelist = ["Rock", "Paper", "Scissors"]

print("Let's play a game")

p_score = 0
cpu_score = 0

rounds = int(input("How many rounds do you play? :"))

round_counter = 0

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

  if player == cpu:
    print("Tie!")

  elif player == "Rock":
    if cpu == "Paper":
      print("CPU beats Player")
      cpu_score += 1
    else:
      print("Player beats CPU")
      p_score += 1

  elif player == "Rock":
    if cpu == "Scissors":
      print("Player beats CPU")
      p_score += 1
    else:
      print("CPU beats Player")
      cpu_score += 1

  elif player == "Paper":
    if cpu == "Scissors":
      print("CPU beats Player")
      cpu_score += 1
    else:
      print("Player beats CPU")
      p_score += 1

  if round_counter == rounds:
    print(f"Player {p_score} : {cpu_score} CPU")
    break


if p_score == cpu_score:
  print("There is no winner, tie.")
elif p_score > cpu_score:
  print("The winner is Player")
elif cpu_score > p_score:
  print("The winner is CPU")