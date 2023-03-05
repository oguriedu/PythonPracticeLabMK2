n=input('Nhập chuỗi:')
so=''
for i in n:
    if i.isnumeric() == True:
        so+=i
print('Các kí tự là số trong string là:',so)
num=int(so)
tong = 0
for j in range(1, num):
    if (num % j) == 0:
        tong += j
if tong == num:
    print('Số',num,'là số hoàn hảo')
else:
    print('Số',num,'Không phải số hoàn hảo')