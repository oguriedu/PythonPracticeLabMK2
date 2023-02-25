a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
x,y=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(f"bội chung nhỏ nhất của {a} và {b} là:{a*b//a} ",)