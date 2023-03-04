n=input("nhap cac chuoi ky tu : ")
print("cac chuoi ky tu vua nhap : ",n)
dem =0
for i in n:
    if "0"<=i<="9":
        dem+=1
print("So cac ky tu trong chuoi :",dem)