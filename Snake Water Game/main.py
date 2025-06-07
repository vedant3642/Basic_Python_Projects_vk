import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("500x600")
root.resizable(False, False)

# Load images
snake_img = ImageTk.PhotoImage(Image.open("snake.png").resize((100, 100)))
water_img = ImageTk.PhotoImage(Image.open("water.png").resize((100, 100)))
gun_img = ImageTk.PhotoImage(Image.open("gun.png").resize((100, 100)))

# Variables
user_score = 0
comp_score = 0
rounds_played = 0
rounds_total = 10

# Mapping
choices = {0: "Snake", 1: "Water", 2: "Gun"}

# Game logic
def check_winner(comp, user):
    if comp == user:
        return 0
    elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return 1  # User wins
    else:
        return -1  # Computer wins

def play(user_choice):
    global user_score, comp_score, rounds_played

    if rounds_played >= rounds_total:
        messagebox.showinfo("Game Over", "Click Reset to play again.")
        return

    comp_choice = random.randint(0, 2)
    result = check_winner(comp_choice, user_choice)

    if result == 0:
        result_text = "Draw!"
    elif result == 1:
        user_score += 1
        result_text = "You Win!"
    else:
        comp_score += 1
        result_text = "Computer Wins!"

    rounds_played += 1
    
    result_label.config(text=f"{result_text}\nYou: {choices[user_choice]} | Computer: {choices[comp_choice]}")
    score_label.config(text=f"You: {user_score} | Computer: {comp_score} | Round: {rounds_played}/{rounds_total}")

def reset_game():
    global user_score, comp_score, rounds_played
    user_score = 0
    comp_score = 0
    rounds_played = 0
    result_label.config(text="")
    score_label.config(text="You: 0 | Computer: 0 | Round: 0/10")

# GUI layout
score_label = tk.Label(root, text="You: 0 | Computer: 0 | Round: 0/10", font=("Helvetica", 16))
score_label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=20)

snake_btn = tk.Button(frame, image=snake_img, command=lambda: play(0))
snake_btn.grid(row=0, column=0, padx=10)

water_btn = tk.Button(frame, image=water_img, command=lambda: play(1))
water_btn.grid(row=0, column=1, padx=10)

gun_btn = tk.Button(frame, image=gun_img, command=lambda: play(2))
gun_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

reset_btn = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_btn.pack(pady=10)

# Run the application
root.mainloop()
