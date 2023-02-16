import math 
def so_nguyen_to(n):
    if n<2:
        return False
    t=int(math.sqrt(n))
    for i in range(2,t+1):
        if (n%i)==0:
            return False
    return True

n=int(input("Vui lòng nhập số nguyên dương:"))
print('Cac so nguyen to khong qua',n,'la:')
if n>=2:
    print(2)
    for i in range(3,n+1):
        if so_nguyen_to(i):
            print(i)
        i=i+2    