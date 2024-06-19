#converts a given string to title case (first
#letter of each word capitalized)

def to_title_case(input_string):
    title_cased_string = input_string.title()
    return title_cased_string

input_string = input("Enter the strings ")
print(to_title_case(input_string))
