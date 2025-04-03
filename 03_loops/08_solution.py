import math

number = int(input("Enter a number: "))
is_prime = True

for i in range(2,math.floor(math.sqrt(number))):
    if number%i == 0:
        is_prime = False
        break

if number == 1 or not is_prime:
    print("The number is not prime.")
elif is_prime:
    print("The number is prime.")