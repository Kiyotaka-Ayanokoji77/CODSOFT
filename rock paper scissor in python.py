import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.user_label = tk.Label(self.root, text="Enter your choice (rock, paper, scissors):")
        self.user_label.grid(row=0, column=0, padx=10, pady=10)
        self.user_entry = tk.Entry(self.root, width=20)
        self.user_entry.grid(row=0, column=1, padx=10, pady=10)
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)
        self.result_entry = tk.Entry(self.root, width=20)
        self.result_entry.grid(row=2, column=1, padx=10, pady=10)

    def play(self):
        user_choice = self.user_entry.get().lower()
        choices = ["rock", "paper", "scissors"]
        if user_choice not in choices:
            messagebox.showerror("Error", "Invalid choice. Please try again.")
            return
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
        else:
            result = "Computer wins!"
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(tk.END, result)

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()
