import string
a = input("Enter Password:")
if len(a) <= 8:
    print("Strong Password")  
else:
    print("Weak Password")