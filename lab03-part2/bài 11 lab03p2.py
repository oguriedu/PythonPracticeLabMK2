a = input('nhập kí tự: ')
n = int (input('nhập số hàng: '))
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print('', end=' ')
    for k in range(1, i+1):
        print(a, end=' ')
    print()