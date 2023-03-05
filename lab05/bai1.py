str=input('mời nhập chuỗi kí tự:')
dem=0
for a in str:
    if '0' <= a <= '9' :
     dem+=1
print('số các kí tự là số trong chuỗi vừa nhập là:',dem)