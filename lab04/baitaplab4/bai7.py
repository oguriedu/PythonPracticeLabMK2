def bc(a,b):
    while (a!=b):
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a
a=int(input("nhập a: "))
b=int(input("nhập b: "))
print("bội chung nhỏ nhất là: ",bc(a,b))