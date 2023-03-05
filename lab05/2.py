n=input("nhap chuoi: ")
print("chuoi nhap vao: ", n)
dem=0
dem2=0
for c in n:
    if "0"<=c<="9":
     dem+=1
for i in n:
    if "a" <= i<= "z"or "b"<=i<="z":
        dem2+=1

print("so chuoi khong phai la tieng anh trong chuoi nhap =",dem)
print("so chuoi khong phai la chuoi so da nhap =",dem2)
