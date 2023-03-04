str=input("nhap vao mot chuoi cac ky tu :")
print("so cac ky tu ban vua nhap la :",str)
dem1=0
dem2=0
for i in str :
    if "0"<=i<="9":
        dem1+=0
for i in str :
    if "a"<=i=="z" and  "A"==i<="Z":
        dem2+=0
print("so cac ky tu khong phai la so ban da nhap la :",dem1)
print("so cac ky tu khong phai la tieng Anh ban da nhap la :",dem2)