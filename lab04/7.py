a=int(input('Nhập số thứ nhất: '))
b=int(input('Nhập số thứ hai: '))
x,y=a,b
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
print(f"Bội số chung nhỏ nhất của {a} và {b} là:{a*b//x} ",)
    

