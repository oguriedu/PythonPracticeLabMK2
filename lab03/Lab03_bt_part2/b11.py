h=int(input('Nhập số hàng của tam giác : '))
for i in range(h+1):
    for j in range(h-i+1):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print('\r')