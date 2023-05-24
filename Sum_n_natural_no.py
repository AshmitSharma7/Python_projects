# This program can find the sum of n natural numbers
num = int(input("Enter the number :"))
Sum = 0
while num > 0:
    Sum += num
    num -= 1

print(Sum)
