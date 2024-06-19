# program that takes a string input from the user and writes it to a
# text file

temp = input("please enter the information")
try:
    with open ("file.txt","w") as file:
        file.write(temp)
except Exception as e:
    print("There is a Problem", str(e))