from random import randrange
import views #if the views file were in a different folde you'd have to put in the path


def evaluate_match(player_choice, computer_choice):
    """ return 'win', 'loss', or 'tie' depending on the match """ 
    if player_choice == "rock":
        if computer_choice == "rock":
            return "tie"
        elif computer_choice == "paper":
            return "loss"
        else:
            return "win"
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "win"
        elif computer_choice == "paper":
            return "tie"
        else:
            return "loss"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "loss"
        elif computer_choice == "paper":
            return "win"
        else:
            return "tie"

def get_computer_choice():
    """ return a random choice from 'rock', 'paper', or 'scissors' """
    computer_choice = randrange(3)
    return ("rock", "paper", "scissors")[computer_choice]

def percents(games, wins, loss, tie):
    print()
    print(f"You played {games} games.")
    print(f"% win: {round((wins / games) * 100, 2)}%")
    print(f"% loss: {round((loss / games) * 100, 2)}%")
    print(f"% tie: {round((tie / games) * 100, 2)}%")


def main():
    games = 0
    wins = 0
    loss = 0
    tie = 0
    
    views.welcome()
    
    while True:
        views.prompt_player()
        player_choice = views.get_player_input()
        print(f' Player choice: {player_choice}')
        result = None
        
        if player_choice == 'exit':
            percents(games, wins, loss, tie)
            break  
        elif player_choice in ("rock", "paper", "scissors"):
            computer_choice = get_computer_choice()
            print(f' Computer choice: {computer_choice}')
            result = evaluate_match(player_choice, computer_choice)
            if result == "win":
                wins +=1
                views.display_win(player_choice, computer_choice)
            elif result == "tie":
                tie += 1
                views.display_tie(player_choice, computer_choice)
            else:
                loss += 1
                views.display_loss(player_choice, computer_choice)
            games += 1
        else:
            views.bad_input()


if __name__ == "__main__":
    main()