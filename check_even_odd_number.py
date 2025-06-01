# Function to check even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Input from user
n = int(input("Enter an integer: "))

# Call the function and store the result
result = is_even(n)

# Check the result and print output
if result:
    print(f"{n} is even")
else:
    print(f"{n} is odd")