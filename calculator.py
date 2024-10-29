import tkinter as tk
from tkinter import messagebox


# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the input and output
entry = tk.Entry(root, width=16, font=("Arial", 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Global variable to keep track of the expression
expression = ""

# Function to update the expression in the entry widget
def button_click(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the final expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result  # update expression with result for next calculation
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# Function to clear the entry widget
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

# Loop to create buttons
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=10, height=2, command=calculate).grid(row=row, column=col, columnspan=2)
    elif button == "C":
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
