num = 10
even_sum = 0
for number in range(num+1):
    if number%2==0:
        even_sum += number

print(f"The even number sum is {even_sum}")