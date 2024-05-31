import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = clicked.get()
        
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set up the dropdown menu for operation selection
options = ["Add", "Subtract", "Multiply", "Divide"]
clicked = tk.StringVar()
clicked.set(options[0])  # Default value

drop = tk.OptionMenu(root, clicked, *options)
drop.grid(row=0, column=1, padx=10, pady=10)

# Create entries for number inputs
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=10, pady=10)

# Create a calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1, padx=10, pady=10)

# Create a result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=1, padx=10, pady=10)

# Adding icons to buttons
def add_icons(button, icon_path):
    icon = Image.open(icon_path)
    icon = icon.resize((20, 20), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon)
    button.config(image=icon)
    button.image = icon

add_icons(calculate_button, "calculate_icon.png")  # Replace with your own icon path

# Run the application
root.mainloop()

