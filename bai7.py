a=int(input('moi nhap so thu nhat: '))
b=int(input('moi nhap so thu hai: '))
x,y=a,b
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
print(f'boi so chung nho nhat cua {a} va {b} la:{a*b//x} ', )