from math import sqrt
try:
    num=int(input("Enter the number: "))
    sqroot=sqrt(num)
    print("Square root of",num,"is",sqroot)
except ValueError:
    print("Input must be an positive integer")


#Enter the number: -5
#Input must be an positive integer
#Enter the number: 56
#Square root of 56 is 7.483314773547883
