# factorial
num=int(input("enter the number"))
fact=1
if num <0 :
    print("sorry, factorial does not exist")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of", num , "is", fact)

