import tkinter as tk
from tkinter import messagebox
import pandas as pd

class AdmissionForm:
    def __init__(self, root):
        # ... (previous code remains unchanged)
        self.root = root
        self.root.title("Admission Form")

        # Set dark mode colors
        bg_color = "#1e1e1e"  # Background color
        fg_color = "#ffffff"  # Foreground color
        text_color = "#dcdcdc"  # Text color

        # Set the font size for big letters
        title_font = ("Helvetica", 24, "bold")

        # Configure root background
        root.config(bg=bg_color)

        # Admission Form title
        title_label = tk.Label(root, text="ADMISSION FORM", font=title_font, bg=bg_color, fg=fg_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Variables to store user inputs
        self.name_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.department_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.class10_var = tk.StringVar()
        self.class12_var = tk.StringVar()

        # Create labels and entry fields
        labels = ['Name:', 'Address:', 'DOB:', 'Department:', 'Email:', 'Phone:', 'Class 10%:', 'Class 12%:']
        for i, label_text in enumerate(labels):
            label = tk.Label(root, text=label_text, bg=bg_color, fg=text_color)
            label.grid(row=i + 1, column=0, sticky='e', padx=10, pady=10)

            entry = tk.Entry(root, bg=bg_color, fg=text_color)
            entry.grid(row=i + 1, column=1, padx=10, pady=10)

            # Assign variables to the corresponding entry fields
            if i == 0:
                entry["textvariable"] = self.name_var
            elif i == 1:
                entry["textvariable"] = self.address_var
            elif i == 2:
                entry["textvariable"] = self.dob_var
            elif i == 3:
                # Create a dropdown list for the 'Department' field
                options = ['CSE', 'IT', 'ECE', 'EE', 'AIML']
                department_dropdown = tk.OptionMenu(root, self.department_var, *options)
                department_dropdown.config(bg=bg_color, fg=text_color)
                department_dropdown.grid(row=i + 1, column=1, padx=10, pady=10, sticky='w')
            elif i == 4:
                entry["textvariable"] = self.email_var
            elif i == 5:
                entry["textvariable"] = self.phone_var
            elif i == 6:
                entry["textvariable"] = self.class10_var
            elif i == 7:
                entry["textvariable"] = self.class12_var

        # Create buttons in horizontal format
        button_frame = tk.Frame(root, bg=bg_color)
        button_frame.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        submit_button = tk.Button(button_frame, text="Submit", command=self.submit_form, bg=bg_color, fg=text_color)
        submit_button.grid(row=0, column=0, padx=10)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_form, bg=bg_color, fg=text_color)
        reset_button.grid(row=0, column=1, padx=10)

        back_button = tk.Button(button_frame, text="Back", command=root.destroy, bg=bg_color, fg=text_color)
        back_button.grid(row=0, column=2, padx=10)

    def submit_form(self):
        # You can perform further actions with the entered data here
        messagebox.showinfo("Submission Successful", "Admission form submitted successfully!")

    def reset_form(self):
        # Reset all input fields
        self.name_var.set("")
        self.address_var.set("")
        self.dob_var.set("")
        self.department_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.class10_var.set("")
        self.class12_var.set("")


    def submit_form(self):
        # Get the data from the entry fields
        data = {
            'Name': self.name_var.get(),
            'Address': self.address_var.get(),
            'DOB': self.dob_var.get(),
            'Department': self.department_var.get(),
            'Email': self.email_var.get(),
            'Phone': self.phone_var.get(),
            'Class 10%': self.class10_var.get(),
            'Class 12%': self.class12_var.get(),
        }

        # Create a DataFrame from the data
        df = pd.DataFrame([data])

        # Save the DataFrame to an Excel file
        excel_file_path = 'admission_data.xlsx'
        try:
            existing_data = pd.read_excel(excel_file_path)
            df = pd.concat([existing_data, df], ignore_index=True)
        except FileNotFoundError:
            pass  # File doesn't exist, ignore and create a new file

        df.to_excel(excel_file_path, index=False)

        # Show a message box indicating successful submission
        messagebox.showinfo("Submission Successful", "Admission form submitted successfully!\nData saved to Excel file.")

    def reset_form(self):
        # Reset all input fields
        self.name_var.set("")
        self.address_var.set("")
        self.dob_var.set("")
        self.department_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.class10_var.set("")
        self.class12_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    admission_form = AdmissionForm(root)
    root.mainloop()
