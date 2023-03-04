#bài 5
str=input('Nhập chuỗi: ')
num=""
char=""
for i in str:
    if i.isnumeric():
        num+=i
    else:
        char+=i
print('Chuối số trong chuỗi là',num)
tong = 0
for j in range(1, int(num)):
    if (int(num) % j) == 0:
        tong += j
if tong == int(num):
    print('Chuỗi số trên là số hoàn hảo')
else:
    print('Chuỗi số trên không phải số hoàn hảo')