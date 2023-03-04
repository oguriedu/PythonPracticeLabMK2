str = int(input("nhap chuoi ki tu:"))
print("chuoi ki tu do la:",str)
a = 0
b = 0
for i in str:
    if i.isalpha():
        a+=1
    if i.isnumeric():
        b+=1
print("so ki tu khong phai la chu cai tieng anh:",a)
print("so ki tu khong phai la so:",b)