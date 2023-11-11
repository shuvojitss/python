import tkinter as tk
def on_click(button_text):
    if button_text == "=":
        try:
            current_text = entry_operation.get()
            result = eval(current_text)
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, str(result))
        except Exception as e:
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, "Error")
    elif button_text == "C":
        entry_operation.delete(0, tk.END)
        entry_result.delete(0, tk.END)
    elif button_text == "<-":
        current_text = entry_operation.get()[:-1]
        entry_operation.delete(0, tk.END)
        entry_operation.insert(tk.END, current_text)
        entry_result.delete(0, tk.END)
    elif button_text == "End":
        root.destroy()  # Close the calculator window
    else:
        entry_operation.insert(tk.END, button_text)
# Create the main window
root = tk.Tk()
root.title("3D Calculator")
root.configure(bg="#222222")  # Set the background color of the window
# Entry widget for current operation
entry_operation = tk.Entry(root, width=20, font=('Helvetica', 20), justify="right", fg="white", bg="#333333", bd=5, relief="ridge")
entry_operation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Entry widget for result display
entry_result = tk.Entry(root, width=20, font=('Helvetica', 20), justify="right", fg="white", bg="#333333", bd=5, relief="ridge")
entry_result.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '<-', '%', 'End'
]
# Add buttons to the grid with thicker margins and closer spacing
row_val = 2
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2, command=lambda b=button_text: on_click(b), fg="white", bg="#555555", bd=5, relief="ridge").grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# Run the main loop
root.mainloop()
