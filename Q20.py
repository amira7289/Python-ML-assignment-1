# program that takes a list of numbers and returns their sum

list1 = [11, 5, 17, 18, 23]
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)