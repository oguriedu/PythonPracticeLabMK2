n=int(input('moi nhap n: '))
x=int(input('moi nhap x: '))
while True:
    if n<=0:
        n=int(input("moi nhap lai n: "))
    if n>0:
        break
#tinh giai thua
def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
cos=1
k=1
for i in range(1,n+1):
    cos+=(((-1)**k)*(x**(2*i)))/tinhgiaithua(2*i)
    k+=1
print(cos)