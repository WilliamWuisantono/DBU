import random

def get_user_input():
    while True:
        user_input = input("Please enter your choice (Rock, Paper, Scissors) or type 'exit' to quit: ").strip().lower()
        if user_input in ['rock', 'paper', 'scissors', 'exit']:
            return user_input
        else:
            print("Invalid choice. Please enter Rock, Paper, Scissors, or exit.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    elif user_choice == 'exit':
        return "exit"
    else:
        return "Computer wins!"

GameOn = True

while GameOn
