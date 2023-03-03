x=input('nhap chuoi : ')
dem=0
for c in x:
 if "0" <= c <= "9":
  dem+=1
print('Số các ký tự là số trong chuỗi trên  =',dem)