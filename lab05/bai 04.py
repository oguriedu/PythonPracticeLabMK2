str1 = input('Nhập str1: ')
str2 = input('Nhập str2: ')
if len(str1)==len(str2):
    for i,j in zip(str1,str2):
        print(i+j,end='')
elif len(str1)>len(str2):
    for i,j in zip(str1,str2):
        print(i+j,end='')
    for i in str1:
        if str1.index(i)<=(len(str2)-1):
            continue
        print(i,end='')
else:
    for i,j in zip(str1,str2):
        print(i+j,end='')
    for i in str2:
        if str2.index(i)<=(len(str1)-1):
            continue
        print(i,end='')
