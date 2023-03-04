str1 = 'Khoa,khoa học ứng dụng'
Lst_str=str1.split(',')
str1=''
for c in Lst_str:
    str1=str1+c+' '
Lst_str=str1.split()
for c in Lst_str:
    print(c)
