a=int(input("Nhập giá trị a = "))
b=int(input("Nhập giá trị b = "))
t = a * b
while a != b :
    if a > b :
        a -= b
    else :
        b -=a
print('BCNN = ', t / a)