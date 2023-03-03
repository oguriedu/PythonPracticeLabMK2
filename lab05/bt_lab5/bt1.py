Str=input('nhập chuỗi kí tự: ')
print('chuỗi vừa nhập: ',Str)
dem =0
for c in Str:
    if "0"<=c<="9":
        dem+=1
print('số các kí tự vừa đếm=',dem)