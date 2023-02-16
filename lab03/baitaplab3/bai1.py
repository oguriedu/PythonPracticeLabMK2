n = int(input('nhập n'))
tong=0
b=1
for i in range(0,n+1):
    b*=2*(n+1)/(2*n+3)
    tong+=b
print(f'{tong}')
