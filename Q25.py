# a program that copies the contents of one text file to another

with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:

    for line in firstfile:

        secondfile.write(line)