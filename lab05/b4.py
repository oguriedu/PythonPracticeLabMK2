
Str1=input('Nhập Str1: ')
Str2=input('Nhập Str2: ')
if len(Str1)==len(Str2):
    for i,j in zip(Str1,Str2):
        print(i+j,end='')
elif len(Str1)>len(Str2):
    for i,j in zip(Str1,Str2):
        print(i+j,end='')
    for i in Str1:
        if Str1.index(i)<=(len(Str2)-1):
            continue
        print(i,end='')
else:
    for i,j in zip(Str1,Str2):
        print(i+j,end='')
    for i in Str2:
        if Str2.index(i)<=(len(Str1)-1):
            continue
        print(i,end='')