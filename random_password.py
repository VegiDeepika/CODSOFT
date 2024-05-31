import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 5:
        return "Password length should be at least 5"
    
    # Ensure the password contains at least one of each required character type
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase), 
        random.choice(string.ascii_lowercase), 
        random.choice(string.digits),          
        random.choice(string.punctuation)       
    ]
    password += random.choices(characters, k=length-4)
    
    random.shuffle(password)
    
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 5:
            raise ValueError
        password = generate_password(length)
        password_display.config(state=tk.NORMAL)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length (minimum 5).")


root = tk.Tk()
root.title("Strong Password Generator")


tk.Label(root, text="Enter the length of the password (minimum 5):").pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

password_display = tk.Entry(root, state='readonly', width=50)
password_display.pack(pady=5)

# Start the GUI event loop
root.mainloop()

