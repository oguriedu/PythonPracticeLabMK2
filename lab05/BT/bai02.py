n=input("nhap cac ky tu : ")
dem=0
for i in n:
    if "0"<=i<="9":
        dem+=1
dem1=0
for i in n:
    if "a"<=i<="z":
        dem1+=1
print("so cac ky tu vua nhap la so :",dem)
print("so cac ky tu vua nhap la tieng anh :",dem1)