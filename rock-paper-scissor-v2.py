import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    
    if player == computer:
        return "It's a tie!"
    
    if player == "rock":
        return "Rock smashes scissors! You win!" if computer == "scissors" else "Paper covers rock! You lose."
    
    if player == "paper":
        return "Paper covers rock! You win!" if computer == "rock" else "Scissors cut paper! You lose."

    if player == "scissors":
        return "Scissors cut paper! You win!" if computer == "paper" else "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
