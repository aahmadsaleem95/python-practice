user_age = int(input("What is your age?: "))
day = input("What day is today?: ").lower()
price = 0
if user_age<18:
    price = 8
else:
    price = 12

if day == "wednesday":
    price -= 2

print(f"Your movie ticket price is: {price}")