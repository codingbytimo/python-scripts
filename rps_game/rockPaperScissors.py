# rock paper scissors command line game by Timo

from turtle import width
from pyfiglet import figlet_format
from termcolor import colored, cprint
from random import randint

# create some variables
user_score = 0
computer_score = 0
rps = ["rock", "paper", "scissors"]

# function for displaying ascii graphics
def art(x):
    graphic = figlet_format(x, "doom", width = 200)
    cprint(graphic, "yellow")
art("rock paper scissors")

# function for printing red text
print_red = lambda x: cprint(x, "red")

while True:
    print("Welcome to a new round of the rock-paper-scissors game! To quit type 'q'")
    # get input from the user
    user_input = input("Please give your input: ")
    # user may quit if q is given as input
    if user_input == "q":
        art("Goodbye.")
        break
    # generate a random number between 0 and 2 to decide the computers choice in the rps array
    randomNumber = randint(0, 2)
    computer_choice = rps[randomNumber]
    # look for invalid input from the user
    if user_input not in rps:
        print_red("Please type in a valid answer!")
    # look if the user input matches the computers choice, if so, it's a tie
    elif computer_choice == user_input:
        print("It's a tie! Try again. " + "User: " + str(user_score), "Computer: " + str(computer_score))
    # look for scenarios where the user wins
    elif user_input == "rock" and computer_choice == "scissors":
        user_score += 1
        print("You win! " + "User: " + str(user_score), "Computer: " + str(computer_score))
    elif user_input == "paper" and computer_choice == "rock":
        user_score += 1
        print("You win! " + "User: " + str(user_score), "Computer: " + str(computer_score))
    elif user_input == "scissors" and computer_choice == "paper":
        user_score += 1
        print("You win! " + "User: " + str(user_score), "Computer: " + str(computer_score))
    # if none of the above scenarios match, the computer wins
    else:
        computer_score += 1
        print("The computer wins! " + "User: " + str(user_score), "Computer: " + str(computer_score))

    # ------------------------------------------------------------------------
    # old implementation
    # ------------------------------------------------------------------------

    ## look for all the other possibilities
    # elif computer_choice == "rock":
    #     if user_input == "scissors":
    #         print("The computer wins!")
    #     elif user_input == "paper":
    #         print("You win!")
    # elif computer_choice == "paper":
    #     if user_input == "rock":
    #         print("The computer wins!")
    #     elif user_input == "scissors":
    #         print("You win!")
    # elif computer_choice == "scissors":
    #     if user_input == "paper":
    #         print("The computer wins!")
    #     elif user_input == "rock":
    #         print("You win!")