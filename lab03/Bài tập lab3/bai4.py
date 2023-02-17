#kiểm tra số nguyên tố
import math
def nguyento(n):
    if n <2 :
        return False
    songuyen=int(math.sqrt(n))
    for i in range (2,songuyen +1):
        if (n%i==0):
            return False
    return True
n=int(input("nhập vào số nguyên dương n: "))
print("các số nguyên tố không quá ",n,"là:")
for i in range (3,n+1):
        if nguyento(i):
            print(i)
        i=i+2
