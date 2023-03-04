a=input('Nhập vào 1 chuỗi là số nhị phân: ')
c=0
for i in range(0,len(a)):
    b=int(a[i])*(2**(len(a)-1-i))
    c+=int(b)
print('Chuyển sang hệ thập phân:',c)