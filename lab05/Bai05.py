str=input('Nhập 1 chuỗi: ')
a=''
for i in str:
    if i.isnumeric():
        a+=i
print('Chuỗi chỉ còn số: ',a)
tong=0
for i in range(1,int(a)):
    if int(a)%i==0:
        tong+=i
if tong==int(a):
    print(a,'là số hoàn hảo')
else:
    print(a,'không là số hoàn hảo')
