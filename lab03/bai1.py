n = int(input('nhập n'))
tong=1
for i in range(1,n):
    tong=tong*2*(n+1)/(2*n+3)
print(f'{tong}')