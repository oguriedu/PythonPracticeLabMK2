import math
n=int(input('Nhập vào số nguyên dương:'))
def ktra_so_nt(n):
    if n<2:
        return False
    for i in range(2,(int)(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True        
for i in range(2,n):
    if ktra_so_nt(i) == True:
        print(i, end="")