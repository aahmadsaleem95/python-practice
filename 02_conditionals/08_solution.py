password = input("Enter your password: ")
pass_chars = len(password)

if pass_chars < 6:
    print("Weak")
elif pass_chars < 11:
    print("Medium")
else:
    print("Strong")