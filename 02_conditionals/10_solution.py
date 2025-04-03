pet_type = input("Enter the pet's specie: ").lower()
age = int(input("Enter the pet's age: "))

if pet_type == 'dog':
    if age < 2 :
        print("Puppy food")
    else:
        print("Adult Dog food")
elif pet_type == 'cat':
    if age <= 5 :
        print("Kitten food")
    else:
        print("Senior cat food")