str=input("nhap vao mot chuoi ky tu :")
print("chuoi ky tu ban da nhap la:")
dem=0
for i in str :
    if "0" <= i <= "9":
        dem+=1
print("so cac ky tu la so la :",dem)