# views.py should have barely anything more than print and input statements

def welcome():
    print("Welcome to Rock, Paper, Scissors")

def prompt_player():
    print("Please select Rock, Paper, Scissors, or Exit")

def get_player_input():
    return input(": ").strip().lower()

def bad_input():
    print("Choice not recognized.")

def display_win(player_choice, computer_choice):
    print(f"{player_choice} beats {computer_choice}, you win.")

def display_tie(player_choice, computer_choice):
    print(f"{player_choice} and {computer_choice} are a tie.")

def display_loss(player_choice, computer_choice):
    print(f"{player_choice} loses to {computer_choice}, computer wins.")