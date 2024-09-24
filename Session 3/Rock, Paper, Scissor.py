#Directions: Create a Rock, Paper, Scissors game that allows the user to play against the computer. The program should prompt the user to enter their choice, then randomly select a choice for the computer. The program should then determine the winner and print the result. The program should continue to play until the user chooses to exit.
#The program should have the following functions:
#Requiements: Save the functions in a separate file called groupex.py and import them into the main program.


#START main
#PRINT welcome message
#CALL a function to get user input and store the result as a variable (user_choice)
#CALL a function to get computer's choice and store the result as variable (computer_choice)
#PRINT both user and computer choices
#CALL a function to decide the winner between two choises (user_choice and computer_choice)
#PRINT the result of the game
#LOOP until the game is over with the user's choice
#END main


#Function to get user input
#Request User Input
#Validate User Input using IN operator and LIST
#Return User Input

#Function to get computer's choice
#Create a list of choices
#Return a random choice from the list
#To use random choices, import random module, and use random.choice() method

#Function to determine the winner
#Compare user's choice and computer's choice
#IF both choices are the same
    #Return "It's a tie!"
#ELSE IF user's choice is rock and computer's choice is scissors
    #Return "You win!"
#ELSE IF user's choice is paper and computer's choice is rock
    #Return "You win!"
#ELSE IF user's choice is scissors and computer's choice is paper
    #Return "You win!"
#ELSE IF user's choice is exit
    #Return "exit"
#ELSE
    #Return "Computer wins!"