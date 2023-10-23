# Function to compare two files
def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            return True
        else:
            return False

# Input file names
file1_name = "file1.txt"
file2_name = "file2.txt"

try:
    if compare_files(file1_name, file2_name):
        print(f"{file1_name} and {file2_name} are identical.")
    else:
        print(f"{file1_name} and {file2_name} are different.")

except FileNotFoundError:
    print("One or both files not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")







#file1.txt and file2.txt are different.
#file1.txt
#Apples are red and guavas are green.
#file2.txt
#The sky is blue.
