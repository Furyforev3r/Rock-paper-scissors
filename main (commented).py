import random # import random module

def Game(): # define function Game
    print("Welcome to Rock, Paper, Scissors!") # print welcome message
    print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.") # print rules
    print("Let's play!")
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ") # get user choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"]) # get computer choice
    if user_choice == computer_choice: # if user choice is equal to computer choice
        print("Tie!") # print tie message
    elif user_choice == "Rock" and computer_choice == "Scissors": # if user choice is Rock and computer choice is Scissors
        print("You win!") # print you win message
    elif user_choice == "Paper" and computer_choice == "Rock": # if user choice is Paper and computer choice is Rock
        print("You win!") # print you win message
    elif user_choice == "Scissors" and computer_choice == "Paper": # if user choice is Scissors and computer choice is Paper
        print("You win!") # print you win message
    else: #if user choise not beats computer choice
        print("You lose!") # print you lose message
    print("The computer chose: " + computer_choice) # print computer choice
    print("Would you like to play again?") # print if user wants to play again
    play_again = input("Enter Y or N: ")
    if play_again == "Y": # if user wants to play again
        Game() # call function Game
    else: # if user doesn't want to play again
        print("Thanks for playing!") # print thanks for playing message
Game() # call function Game