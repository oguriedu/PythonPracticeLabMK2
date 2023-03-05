
chuoi = input('Nhập chuỗi: ')
num = ''
char = ''
tong = 0
for i in chuoi:
    if i.isnumeric():
        num+=i
    else:
        char+=i
print('Chuỗi số trong str là: ',num)
for i in range(1, int(num)):
    if int(num)%i==0:
        tong+=i
if tong == int(num):
    print('Chuỗi là số hoàn hảo ')
else:
    print('Chuỗi không phải số hoàn hảo ')