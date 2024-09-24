from groupex import *

GameOn = True

while GameOn:
    print("Welcome to Rock, Paper, Scissors! Please enter your choice.")
    user_choice = get_user_input()
    print("You chose: ", user_choice)
    if user_choice == 'exit':
        GameOn = False
        print("Thanks for playing!")
        break

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(user_choice, computer_choice)
    print(result)