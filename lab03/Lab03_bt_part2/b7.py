n=int(input('Nhập số n:'))
S=0
for i in range(1,n+1):
    m=1/i
    print(m)
    S+=m
print('Tổng nghịch đảo n số đầu tiên là:',S)