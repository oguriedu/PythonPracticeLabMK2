n=int(input('Nhập vào số nguyên dương:'))
def ktra_snt(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True        
for i in range(2,n):
    if ktra_snt(i) == True:
        print(i, end=" ")
