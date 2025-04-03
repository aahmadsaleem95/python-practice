year = int(input("Enter the year: "))
# year%400 == 0 or (year%4==0 and year%100!=0)
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("A leap year")
        else:
            print("Not a leap year")
    else:
        print("A leap year")
else:
    print("Not a leap year")