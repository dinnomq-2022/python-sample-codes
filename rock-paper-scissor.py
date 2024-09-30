import random


def get_choices():

  player_choice = input ("Enter a choice (rock, paper, scissors: ")
  option = ["rock", "paper", "scissors"]
  computer_choice = random.choice(option)
  choices = {"player": player_choice, "computer": computer_choice }
  

  return choices

def check_win(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player == computer:
    return "It's a tie!"
    
  elif player == "rock":
    if computer == "scissor":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."

  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissor cuts paper. You lose."   

  elif player == "scissor":
    if computer == "paper":
      return "Paper covers rock! You win!"
    else:
      return "Rock smashes scissor. You lose."      
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



