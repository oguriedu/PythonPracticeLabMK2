a=float(input("Nhập số thập phân:"))
so=[]
dem=["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
for i in str(a):
    if i==".":
        continue
    else:
        so.append(i)
chuoi=" "
for num in so:
    for j in range(0,len(dem)):
        if int(num)==j:
            chuoi+=dem[j]
            chuoi+=" "
print(a)
print(chuoi)

