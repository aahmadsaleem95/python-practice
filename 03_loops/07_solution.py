number = int(input("Enter a number between 1 and 10: "))

while number < 1 or number > 10:
    number = int(input("You entered and invalid number. Please enter a number between 1 and 10: "))

print("The number is ", number)