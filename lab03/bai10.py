n = int(input('Nhập n:'))
print('thừa số nguyên tố của %i là: '%(n),end='')
for i in range(2,n+1):
    dem = 0
    while n%i == 0:
        dem +=1
        n /= i
    if dem:
        if dem > 1:
            print('%i^%i'%(i,dem),end='')
        else:
            print(i,end='')
        if n > i:
            print('+',end='')
    