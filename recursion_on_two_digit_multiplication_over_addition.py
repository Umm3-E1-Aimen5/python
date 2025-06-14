def multiplication(n1,n2):
    n = 0
    if n2 != 0:
        n = n1 + multiplication(n1,n2-1)
    return n    


            



product = multiplication(5,10)  
print(product)    