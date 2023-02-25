a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
x,y=a,b
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
print(f"bội chung nhỏ nhất của {a} và {b} là:{a*b//x} ",)