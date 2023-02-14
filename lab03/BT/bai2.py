x = int(input("Nhập số nguyên x:"))
def shh(x):
    tong = 0
    for i in range(1,x):
        if x%i==0 :
            tong+=i
    if tong == x:    
        return True
    return False
def liet_ke(x):
    for i in range (1,x):
        if shh(i):
            print(i)
liet_ke(x)
