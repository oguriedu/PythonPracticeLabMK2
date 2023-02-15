n=int(input('Nhập n = '))
s=1
a=1
for n in range(0,n+1):
    a*=((2*(n+1))/(2*n+3))
    s+=a
print(f'Kết quả: {s:.3f}')