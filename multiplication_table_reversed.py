# This program can display the multiplication table (IN REVERSED ORDER) of given Integer 
num = int(input("Enter the Number :"))
ls = list(range(11))
ls.reverse()
for i in ls:
    print(f"{num} X {i} = {num*i}")
