import random

def Game():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("Let's play!")
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("You lose!")
    print("The computer chose: " + computer_choice)
    print("Would you like to play again?")
    play_again = input("Enter Y or N: ")
    if play_again == "Y":
        Game()
    else:
        print("Thanks for playing!")
Game()