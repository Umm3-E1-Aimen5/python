# Define the compute_factorial() function
def compute_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial    

# Get the user input
number = int(input("Enter a positive integer: "))

total = compute_factorial(number)
print(total)