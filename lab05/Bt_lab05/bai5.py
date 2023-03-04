n=input('Nhập giá trị:')
kq=''
for i in n:
    if i.isnumeric():
        kq+=str(i)
print('Chuỗi còn lại là:',kq)
so=int(kq)
s=0
for k in range(1,so):
    if so%k==0:
        s+=k
if s==so:
    print('Chuỗi số này là số hoàn hảo')
else:
    print('Chuỗi số này không phải là số hoàn hảo')
        