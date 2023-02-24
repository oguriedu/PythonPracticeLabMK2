# bài 7
a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
x,y=a,b
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
bcnn=(a*b)//x
print("bội chung nn : ",bcnn)