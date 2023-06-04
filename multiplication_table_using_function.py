def table(n):
    for i in range(11):
        res = i * n
        print(f"{n} X {i} = {res}")


num = int(input("Number ? :"))
result = table(num)
print(result)
