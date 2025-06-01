'''
Write a program to find the smallest of three numbers.


Get three integer inputs: n1, n2 and n3.
Find the smallest number and display it.

'''
def get_smallest_number(n1,n2,n3):
    if(n1 >= n2) and (n3 >= n2):
        return n2
    elif(n2 >= n3) and (n1 >= n3):
        return n3
    else:
        return n1    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))    
smallest_number = get_smallest_number(num1,num2,num3)
print(smallest_number)
 