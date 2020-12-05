# Incorporate the random library
import random
# Print Title

print("Let's play rock paper scissors!")
# Specify the three options
options = ["r", "p", "s"]
again = 'y'
while again.lower() == 'y':
    # Computer Selection
    computer_choice = random.choice(options)
    # User Selection
    user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors?")
    # Run Conditionals
    if computer_choice == user_choice: 
        print(f"computer_choice is: {computer_choice}")
        print("We are tie")
    if computer_choice == "p" and user_choice == "r":
        print(f"computer_choice is: {computer_choice}")
        print("I loose")
    if computer_choice == "s" and user_choice == "r":
        print(f"computer_choice is: {computer_choice}")
        print("I win")
    if computer_choice == "r" and user_choice == "p":
        print(f"computer_choice is: {computer_choice}")
        print("I win")
    if computer_choice == "s" and user_choice == "p":
        print(f"computer_choice is: {computer_choice}")
        print("I loose")
    if computer_choice == "r" and user_choice == "s":
        print(f"computer_choice is: {computer_choice}")
        print("I loose")
    if computer_choice == "p" and user_choice == "s":
        print(f"computer_choice is: {computer_choice}")
        print("I win")
    again = input("Would you like to try this again? (Y/N)")