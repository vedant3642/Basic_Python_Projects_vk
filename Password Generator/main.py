import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_special_chars = special_chars_var.get()

        # Define the character sets
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        # Start with lowercase characters as the base
        char_pool = lowercase_chars

        if use_uppercase:
            char_pool += uppercase_chars
        if use_numbers:
            char_pool += digits
        if use_special_chars:
            char_pool += special_chars

        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return

        # Generate a random password
        password = ''.join(random.choice(char_pool) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# UI Elements
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50").pack(pady=10)
tk.Label(root, text="Password Length:", font=("Arial", 12), fg="white", bg="#2C3E50").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=("Arial", 10), bg="#2C3E50", fg="white", selectcolor="#34495E")
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Arial", 10), bg="#2C3E50", fg="white", selectcolor="#34495E")
special_chars_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var, font=("Arial", 10), bg="#2C3E50", fg="white", selectcolor="#34495E")

uppercase_check.pack()
numbers_check.pack()
special_chars_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", padx=10, pady=5)
generate_button.pack(pady=15)

# Password entry field
password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
