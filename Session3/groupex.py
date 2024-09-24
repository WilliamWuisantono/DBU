import random

def get_user_input():
        user_input = input("Please enter your choice (Rock, Paper, Scissors) or type 'exit' to quit: ")
        if user_input in ['Rock', 'Paper', 'Scissors', 'exit']:
            return user_input
        else:
            return "Invalid choice. Please enter Rock, Paper, Scissors, or exit."

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        return "You win!"
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        return "You win!"
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        return "You win!"
    elif user_choice == 'exit':
        return "exit"
    else:
        return "Computer wins!"
