import tkinter as tk
from tkinter import ttk
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        return

    # Set properties
    selected_voice = voice_var.get()
    if selected_voice == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', rate_slider.get())
    engine.setProperty('volume', volume_slider.get())

    # Speak
    engine.say(text)
    engine.runAndWait()

# GUI setup
app = tk.Tk()
app.title("Professional Text-to-Speech")
app.geometry("500x500")  # Increased height
app.configure(bg="#f5f5f5")

# Title
tk.Label(app, text="Text-to-Speech Converter", font=("Helvetica", 18, "bold"), bg="#f5f5f5").pack(pady=10)

# Text input
tk.Label(app, text="Enter Text:", font=("Helvetica", 12), bg="#f5f5f5").pack(anchor="w", padx=20)
text_entry = tk.Text(app, height=5, width=50, font=("Helvetica", 12))
text_entry.pack(padx=20, pady=5)

# Voice selection
voice_var = tk.StringVar(value="Male")
tk.Label(app, text="Select Voice:", font=("Helvetica", 12), bg="#f5f5f5").pack(anchor="w", padx=20, pady=(10, 0))
voice_combo = ttk.Combobox(app, textvariable=voice_var, values=["Male", "Female"], state="readonly")
voice_combo.pack(padx=20, anchor="w")

# Rate slider
tk.Label(app, text="Speech Rate:", font=("Helvetica", 12), bg="#f5f5f5").pack(anchor="w", padx=20, pady=(10, 0))
rate_slider = tk.Scale(app, from_=100, to=250, orient="horizontal", length=200)
rate_slider.set(150)
rate_slider.pack(padx=20, anchor="w")

# Volume slider
tk.Label(app, text="Volume:", font=("Helvetica", 12), bg="#f5f5f5").pack(anchor="w", padx=20, pady=(10, 0))
volume_slider = tk.Scale(app, from_=0.0, to=1.0, resolution=0.1, orient="horizontal", length=200)
volume_slider.set(1.0)
volume_slider.pack(padx=20, anchor="w")

# Speak button
b = ttk.Button(app, text="Speak", command=speak_text)
b.pack(pady=20)

app.mainloop()
