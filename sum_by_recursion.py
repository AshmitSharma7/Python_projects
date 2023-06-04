def rec(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return n + rec(n-1)



num = int(input("Enter a Number :"))
result = rec(num)
print(result)