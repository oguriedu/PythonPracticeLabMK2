str1=input('moi nhap chuoi thu 1: ')
str2=input('moi nhap chuoi thu 2: ')
l=[]
for i in str1:
    for j in str2:
        if i == j:
            l+=i
print('Các kí tự chung là:',l)
max=len(str1)
if len(str2)>len(str1):
    max=len(str2)
else:
    max=len(str1)
print('Chuỗi có độ dài cực đaị là:',max)