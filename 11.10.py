# Function to toggle the case of letters in a text and save it to another file
def toggle_case(input_file, output_file):
    try:
        with open(input_file, "r") as input_file:
            text = input_file.read()
            toggled_text = "".join([char.lower() if char.isupper() else char.upper() if char.islower() else char for char in text])

        with open(output_file, "w") as output_file:
            output_file.write(toggled_text)

        print(f"Text from '{input_file}' has been case-toggled and saved to '{output_file}'.")

    except FileNotFoundError:
        print("One or both files not found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input file name
input_file_name = "input.txt"
# Output file name
output_file_name = "output.txt"

# Toggle the case of letters and save it to the output file
toggle_case(input_file_name, output_file_name)




#input.txt
#I am a student
#output.txt
#i AM A STUDENT

