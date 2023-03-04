n = input("Nhap chuoi ky tu:")

count1=0
count2=0

for  i in n:
    if "0" <= i <= "9":
        count1 += 1
for i in n:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        count2 += 1

print("So cac ky tu khong phai tieng anh:", count1)
print("So cac ky tu khong phai so:", count2)