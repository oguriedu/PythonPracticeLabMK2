n = int(input('Nhập số n: '))
if n == 1:
    print('Không có số lẻ < 1!')
else:
    print("Các số lẻ nhỏ hơn n là: ")
    for i in range(1, n+1, 2):
        if i == n:
            break
        print(i, '', end="")
