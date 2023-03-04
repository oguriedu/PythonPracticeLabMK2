str1=input('Nhập chuỗi 1: ')
str2=input('Nhập chuỗi 2: ')
b=''
for i in range(0,min(len(str1),len(str2))):
    a=str1[i]+str2[i]
    b+=a
if len(str1)>len(str2):
    c=b+str1[min(len(str1),len(str2)):]
else:
    c=b+str2[min(len(str1),len(str2)):]
print(c)