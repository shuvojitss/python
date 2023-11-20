import tkinter as tk

def on_click(button_text):
    # Function to handle button clicks

    if button_text == "=":
        try:
            # Evaluate the expression and display the result
            current_text = entry_operation.get()
            current_text = current_text.replace('^', '**')
            current_text = current_text.replace('%', '*0.01')
            result = eval(current_text)
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, str(result))
        except Exception as e:
            # Handle errors and display "Error" in the result field
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, "Error")
    elif button_text == "C":
        # Clear the input and result fields
        entry_operation.delete(0, tk.END)
        entry_result.delete(0, tk.END)
    elif button_text == "<-":
        # Delete the last character in the input field
        current_text = entry_operation.get()[:-1]
        entry_operation.delete(0, tk.END)
        entry_operation.insert(tk.END, current_text)
        entry_result.delete(0, tk.END)
    elif button_text == "+/-":
        # Change the sign of the current input
        current_text = entry_operation.get()
        if current_text and current_text[0] == '-':
            entry_operation.delete(0)
        else:
            entry_operation.insert(0, '-')
    elif button_text == "End":
        # Close the calculator
        root.destroy()
    elif button_text == "%":
        # Insert "*0.01" in the input field for percentage
        entry_operation.insert(tk.END, "*0.01")
    else:
        # Insert the clicked button's text in the input field
        entry_operation.insert(tk.END, button_text)

def on_key(event):
    # Function to handle key events

    key = event.char
    if key.isdigit() or key in {'+', '-', '*', '/', '.', '^', '(', ')'}:
        # If the key is a digit or basic operator, handle it as a button click
        on_click(key)
    elif key == '\x08':  # Backspace
        # Handle Backspace key as a "<-" button click
        on_click("<-")
    elif key == '\r':  # Enter
        # Handle Enter key as an "=" button click
        on_click("=")

# Create the main window
root = tk.Tk()
root.title("3D Calculator")
root.configure(bg="#222222")

# Entry widgets for displaying input expression and result
entry_operation = tk.Entry(root, width=15, font=('Helvetica', 18), justify="right", fg="white", bg="#333333", bd=5, relief="ridge")
entry_operation.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

entry_result = tk.Entry(root, width=15, font=('Helvetica', 18), justify="right", fg="white", bg="#333333", bd=5, relief="ridge")
entry_result.grid(row=3, column=0, padx=10, pady=10)

# Buttons for calculator operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '<-', '%', 'End',
    '^', '(', ')', '+/-'
]

# Initialize row and column values for grid layout
row_val = 0
col_val = 1

# Create buttons and arrange them in a grid layout
for button_text in buttons:
    if button_text == "End":
        # Special styling for the "End" button
        tk.Button(root, text=button_text, width=4, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="red", bd=5, relief="raised").grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button_text == "C":
        # Special styling for the "C" button
        tk.Button(root, text=button_text, width=4, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="green", bd=5, relief="raised").grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button_text in {'<-', '%', '+/-'}:
        # Special styling for specific buttons
        tk.Button(root, text=button_text, width=4, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="blue", bd=5, relief="raised").grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button_text in {'^', '(', ')'}:
        # Special styling for specific buttons
        tk.Button(root, text=button_text, width=4, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="#555555", bd=5, relief="raised").grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        # Default styling for other buttons
        tk.Button(root, text=button_text, width=4, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="#333333", bd=5, relief="raised", overrelief="sunken").grid(row=row_val, column=col_val, padx=5, pady=5)
    
    # Increment column value, reset to 1 if it exceeds 4
    col_val += 1
    if col_val > 4:
        col_val = 1
        row_val += 1

# Set window transparency
root.attributes("-alpha", 0.8)

# Bind the on_key function to key events
root.bind('<Key>', on_key)

# Start the main event loop
root.mainloop()
