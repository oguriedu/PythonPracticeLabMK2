#2
n=int(input('Nhập n: '))
print('Số hoàn hảo nhỏ hơn n là: ',end="")
for i in range(1,n):
    tong = 0
    for j in range(1, i):
        if (i % j) == 0:
            tong += j
    if tong == i:
        print(i,end=' ')