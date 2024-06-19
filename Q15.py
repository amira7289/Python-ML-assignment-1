#a program that reads data from a CSV file and prints it to the
#console.

import csv

def read_and_print_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                for element in row:
                    print(element, end=' ')
                print()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'file.csv'
read_and_print_csv(file_path)