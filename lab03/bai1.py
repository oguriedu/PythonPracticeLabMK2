n=int(input('Nhap n :'))
S=0
a=1
for i in range(1,n+1):
    a*=(2*(n+1))/(2*n+3)
    S+=a
print(round(S,2))