# This is the program to find vowels in a string

vowel = "aeiou"
user_inp = input("Enter a String :")

a = [v for v in user_inp if v in vowel]

print(len(a))
print(a)
