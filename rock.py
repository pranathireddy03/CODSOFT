import tkinter as tk
import random

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

# Function to simulate computer's choice
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# Function to handle user's choice
def user_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: user_choice('Rock'))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: user_choice('Paper'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice('Scissors'))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
