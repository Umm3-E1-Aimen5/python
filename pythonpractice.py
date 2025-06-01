integer_num = 123
float_num =  1.23
sum_num = integer_num + float_num
print("value:",sum_num)
print("data type:",type(sum_num))   # implicit conversion

num_string = '12'
num_integer = 23
print("data type before typecasting:",type(num_string))
num_string = int(num_string)
print("data type after type conversion :",type(num_string))
num_sum = num_string + num_integer
print("sum of numbers: ",num_sum)
print("data type of num_sum is :",type(num_sum))   # explicit conversion
print("Good Morning!",end ='')
print("its rainy today")
print('New Year',2023,'see you soon',sep ='.')
print(5)
print('programiz is '+'awesome')