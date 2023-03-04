chuoi=input("moi nhap chuoi: ")
lon_nhat=0
for i in chuoi:
    dem=chuoi.count(i)
    max=lon_nhat
    if dem>lon_nhat:
        lon_nhat=dem
for j in chuoi:
    if chuoi.count(j)==lon_nhat:
        print(end=j)
