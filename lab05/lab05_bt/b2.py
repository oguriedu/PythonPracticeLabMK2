str=input('nhập chuỗi kí tự :')
dem_chu=0
dem_so=0
for i in str:
    if 'a'<= i <='z' or 'A'<= i <='Z':
       'các kí tự kiếng anh'
    else:
        dem_chu+=1
print('có',dem_chu,'kí tự kh phải tiếng anh')
for j in str:
    if '0' <= j <= '9':
        'các kí tự số'
    else:
        dem_so+=1
print('có',dem_so,'kí tự kh phải số ')