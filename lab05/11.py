Str1 = 'Khoa,khoa học ứng dụng'
Lst_Str=Str1.split(',')
Str1=''
for c in Lst_Str:
    Str1=Str1+c+' '
Lst_Str=Str1.split()
for c in Lst_Str:
    print(c)
