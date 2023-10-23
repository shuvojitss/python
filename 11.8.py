# Function to reverse a string
def reverse_text(text):
    return text[::-1]

# Input file name
input_file_name = "input.txt"
# Output file name
output_file_name = "output.txt"

try:
    # Read text from the input file
    with open(input_file_name, "r") as input_file:
        text = input_file.read()

    # Reverse the text
    reversed_text = reverse_text(text)

    # Write the reversed text to the output file
    with open(output_file_name, "w") as output_file:
        output_file.write(reversed_text)

    # Display the reversed text
    print("Reversed text:")
    print(reversed_text)

except FileNotFoundError:
    print(f"File not found: {input_file_name}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
