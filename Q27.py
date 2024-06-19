# a program in python that converts a string into a list of its characters

def string_to_list(string):
    # Convert the string to a list of characters
    char_list = list(string)
    return char_list

# Example usage
string = input("Enter the String ")
char_list = string_to_list(string)
print(char_list)
