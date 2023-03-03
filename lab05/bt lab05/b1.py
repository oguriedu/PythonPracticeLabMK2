str = input('nhập chuỗi kí tự : ')
đem_so = 0
for i in str:
    if i >= '0' and i <= '9':
        đem_so += 1
print ('số kí tự là số trong chuỗi vừa nhập = ', đem_so)