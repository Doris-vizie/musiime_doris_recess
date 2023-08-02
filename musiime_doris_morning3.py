# tkinter learn 
# Assignment create a simple calculator program with a GUI interface.
# Make the title of the calculator program window with your name
import tkinter as tk

def add_digit(digit):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(digit))

def add_operator(operator):
    current_text = entry.get()
    if current_text and current_text[-1].isdigit():
        entry.insert(tk.END, operator)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Doris' Calculator")

# Create the entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the digit buttons
digits = "789456123"
for i, digit in enumerate(digits):
    button = tk.Button(window, text=digit, padx=15, pady=10, command=lambda digit=digit: add_digit(digit))
    button.grid(row=1 + i // 3, column=i % 3)

# Create the operator buttons
operators = "+-*/"
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, padx=15, pady=10, command=lambda operator=operator: add_operator(operator))
    button.grid(row=1 + i, column=3)

# Create the equal button
equal_button = tk.Button(window, text="=", padx=15, pady=10, command=calculate)
equal_button.grid(row=4, column=2)

# Create the clear button
clear_button = tk.Button(window, text="C", padx=15, pady=10, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=4, column=0)

# Start the GUI event loop
window.mainloop()
