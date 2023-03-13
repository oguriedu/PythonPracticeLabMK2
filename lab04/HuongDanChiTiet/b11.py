n = int(input('Nhập n:'))
print('Các số nguyên tố từ 1 đến ', n, 'là:')
i = int(2)
while (i <= n):
    kt = 1
    if i != 0 and i != 1:
        j = int(2)
        while (j <= i/2):
            if i % j == 0:
                kt = 0
                break
            j += 1
    else:
        kt = 0
    if kt == 1:
        print(i, ' ', end='')
    i += 1
