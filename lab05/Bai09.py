str1=input('Nhập chuỗi 1: ')
str2=input('Nhập chuỗi 2: ')
ky_tu_chung=[]
for i in str1:
    if str2.count(i)>0:
        ky_tu_chung.append(i)
for i in ky_tu_chung:
    a=str1.count(i)
    b=str2.count(i)
    if a>b:
        kq1=i*a
        kq2=i*b
    else:
        kq1=i*b
        kq2=i*a
if len(kq1)>len(kq2):
    print('Kí tự chung và có độ dài cực đại là: ',kq1)
else:
    print('Kí tự chung và có độ dài cực đại là: ',kq2)
