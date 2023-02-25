a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
x,y=a,b
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
BCNN=(a*b)//x
print("bội chung nhỏ nhất là : ",BCNN)