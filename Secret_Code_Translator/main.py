import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

def encode_message(message, pwd):
    words = message.split(" ")
    encoded = []
    for word in words:
        if len(word) >= 3:
            rand_prefix = "".join(random.choices(string.ascii_lowercase, k=pwd))
            rand_suffix = "".join(random.choices(string.ascii_lowercase, k=pwd))
            new_word = rand_prefix + word[1:] + word[0] + rand_suffix
            encoded.append(new_word)
        else:
            encoded.append(word[::-1])
    return " ".join(encoded)

def decode_message(message, pwd):
    words = message.split(" ")
    decoded = []
    for word in words:
        if len(word) >= 3:
            trimmed = word[pwd:-pwd]
            original = trimmed[-1] + trimmed[:-1]
            decoded.append(original)
        else:
            decoded.append(word[::-1])
    return " ".join(decoded)

def process():
    try:
        mode = mode_var.get()
        pwd = int(password_var.get())
        if pwd not in [3, 4, 5]:
            raise ValueError("Password must be 3, 4 or 5")
        msg = input_text.get("1.0", tk.END).strip()

        if not msg:
            messagebox.showwarning("Empty Input", "Please enter a message.")
            return

        if mode == "Encode":
            result = encode_message(msg, pwd)
        else:
            result = decode_message(msg, pwd)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Secret Code Translator")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Secret Code Translator", font=("Arial", 16)).pack(pady=10)

# Mode selection
mode_var = tk.StringVar(value="Encode")
tk.Label(root, text="Choose Mode:").pack()
ttk.Combobox(root, textvariable=mode_var, values=["Encode", "Decode"], state="readonly").pack(pady=5)

# Password input
tk.Label(root, text="Enter Password (3, 4 or 5):").pack()
password_var = tk.StringVar(value="3")
tk.Entry(root, textvariable=password_var).pack(pady=5)

# Input message
tk.Label(root, text="Enter Your Message:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

# Button
tk.Button(root, text="Process", command=process).pack(pady=10)

# Output message
tk.Label(root, text="Result:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

root.mainloop()
