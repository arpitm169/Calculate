import tkinter as tk
from tkinter import messagebox
import os

def history(num1, num2, calc, operation):
    with open("history.txt", "a") as my_file:
        my_file.write(f"{num1} {operation} {num2} = {calc}\n")

def timer():
    time_label.config(text="Calculating...")
    window.after(1000, lambda: time_label.config(text=""))

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        result_label.config(text=f"Result: {result}")
        history(num1, num2, result, operation)
        timer()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def show_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as my_file:
            history_content = my_file.read()
            messagebox.showinfo("History", history_content)
    else:
        messagebox.showinfo("History", "No history available yet")

def quit_program():
    window.destroy()

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")

# Number inputs
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)

# Operation buttons
button_add = tk.Button(window, text="Add (+)", command=lambda: calculate('+'))
button_add.grid(row=2, column=0)

button_subtract = tk.Button(window, text="Subtract (-)", command=lambda: calculate('-'))
button_subtract.grid(row=2, column=1)

button_multiply = tk.Button(window, text="Multiply ()", command=lambda: calculate(''))
button_multiply.grid(row=3, column=0)

button_divide = tk.Button(window, text="Divide (/)", command=lambda: calculate('/'))
button_divide.grid(row=3, column=1)

# History and quit buttons
button_history = tk.Button(window, text="Show History", command=show_history)
button_history.grid(row=4, column=0)

button_quit = tk.Button(window, text="Quit", command=quit_program)
button_quit.grid(row=4, column=1)

# Result and timer display
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

time_label = tk.Label(window, text="")
time_label.grid(row=6, column=0, columnspan=2)

# Start the main loop
window.mainloop()
