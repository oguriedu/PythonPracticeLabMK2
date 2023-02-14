import math
x = eval (input('nhập số x: '))
f = ((-x)+math.sqrt(math.pow(x,2)+4))/(math.pow(math.pow(x,4)+1,1/7))
print ('giá trị của biểu thức là: ', round(f, 2))
