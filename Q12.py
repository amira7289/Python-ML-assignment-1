#calculates the sum of the digits of a given
#number

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = int(input("Enter number - "))
print(getSum(n))