'''
Largest of Three Numbers
We will now build the logic to find the largest number among n1, n2, and n3.

We know n1 is the largest number if:

n1 is greater than n2, and
n1 is greater than n3
Similarly, we can check if n2 or n3 is largest using the same logic. To solve this problem, we can use the and operator.

'''

def get_largest_number(n1,n2,n3):
    if(n1 >= n2) and (n1 >= n3):
        return n1
    elif(n2 >= n3) and (n2 >= n1):
        return n2
    else:
        return n3    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))    
largest_number = get_largest_number(num1,num2,num3)
print(largest_number)