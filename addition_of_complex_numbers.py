class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag


    def add(self,number): 
        real_result = self.real + number.real
        imag_result = self.imag + number.imag
        result = complex(real_result,imag_result)   
        return result


n1 = complex(5,6)
n2 = complex(-4,2)   

n3 = n1.add(n2)

print('real part = ',n3.real)
print('imaginary part = ',n3.imag)