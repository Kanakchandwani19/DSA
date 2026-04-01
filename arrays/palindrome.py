n = input("Enter string: ")

a = n[0::]
b = n[::-1]

if (a==b):
    print("Palindrome.")
else:
    print("Not Palindrome.")