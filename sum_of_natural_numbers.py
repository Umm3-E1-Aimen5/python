def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum
n = int(input("Enter any number:"))
sum = sum_of_natural_numbers(n)    
print(sum)
