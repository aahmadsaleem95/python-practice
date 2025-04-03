coffee_size = input("Coffee size: ")
extra_shot = True if input("Want an extra shot?").lower() == 'yes' else False

print(f"{coffee_size} {"coffee with an extra shot" if extra_shot else "" }")