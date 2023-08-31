import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for length.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter the desired length:", bg="#f0f0f0")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password: ", bg="#f0f0f0")
password_label.pack()

# Start the main event loop
root.mainloop()
