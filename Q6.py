# program that reads the content of a text file and prints it to the
# console

file_path = 'file.txt'

try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content
        print("File Content:\n", file_content)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")