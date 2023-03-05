str = input('nhập chuỗi kí tự : ')
dem_so = 0
dem_chu = 0
for i in str:
    if i >= '0' and i <= '9':
        dem_so += 1
for j in str:
    if (j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z'):
        dem_chu += 1
print('số kí tự là số trong chuỗi vừa nhập =', dem_so)
print('số kí tự là chữ trong chuỗi vừa nhập =', dem_chu)