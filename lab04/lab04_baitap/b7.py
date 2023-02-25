a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
x,y=a,b
while x!= y:
    if x>y :
        x-=y
    else:
        y-=x
print("Bội chung nhỏ nhất của hai số nguyên",a,"và",b,"là:",a*b//x)