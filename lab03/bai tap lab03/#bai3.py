#bai3
n=int(input('Nhập số cần kiểm tra:'))
check=True
if (n<2):
    check=False
for i in range(2,n):
    if (n % i == 0):
        check = False
if check:
    print(n,'là số nguyên tố')
else:
    print(n,'không phải số nguyên tố')
