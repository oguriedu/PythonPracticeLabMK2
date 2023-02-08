import math

def bt(x):
    m=(math.log(4,x))+(math.log(x,2))
    return m
x=eval(input("Nhập giá trị x = "))
if x>0 and x!=1:
   print('Giá trị của biểu thức là: ',round(bt(x),2))
else:
 print("Nhập giá trị lỗi, hãy nhập lại")

 