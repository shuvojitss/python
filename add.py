import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

def reset_values():
    entry_num1.delete(0, 'end')
    entry_num2.delete(0, 'end')
    result_label.config(text="Result: ")

def exit_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("ADD")

# Set the size of the window
window.geometry("400x200")

# Create input fields
label_num1 = tk.Label(window, text="Enter !st no:")
entry_num1 = tk.Entry(window)
label_num2 = tk.Label(window, text="Enter 2nd no:")
entry_num2 = tk.Entry(window)

# Create the Add, Reset, and Exit buttons
add_button = tk.Button(window, text="ADD", command=add_numbers)
reset_button = tk.Button(window, text="RESET", command=reset_values)
exit_button = tk.Button(window, text="END", command=exit_program)

# Place widgets on the window using the grid layout
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1.grid(row=0, column=1, padx=10, pady=10)
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)
add_button.grid(row=2, column=0, padx=10, pady=10)
reset_button.grid(row=2, column=1, padx=10, pady=10)
exit_button.grid(row=2, column=2, padx=10, pady=10)
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, columnspan=3, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
