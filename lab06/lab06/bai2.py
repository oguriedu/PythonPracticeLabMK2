n=int(input("nhap so phan tu cua danh sach nhap vao: "))
danh_sach=[]

for i in range(n):
    danh_sach.append(int(input(f"moi nhap phan tu thu {i+1}: ")))
b=danh_sach.copy()
b.sort()
lon_nhi=b[-2]
cong=0
so_sanh=0
duong=[]
duong_lien_tiep=[]
so_lon_nhi=0
for j in danh_sach:
    if j==lon_nhi:
        so_lon_nhi+=1
    if j>=0:
        cong+=1
        duong.append(j)
    if j<0:
        k=0
        cong=0
        duong_lien_tiep.insert(k,duong)
        k+=1
        duong=[]
    if cong>so_sanh:
        so_sanh=cong
if duong != [] and len(duong)>1:
    duong_lien_tiep.insert(k,duong)
tong_max=0
for l in range(0,len(duong_lien_tiep)):
    tong=0
    for m in duong_lien_tiep[l]:
        tong+=m
    if tong>tong_max:
        tong_max=tong
# Tính số lượng các số dương liên tiếp có tổng lớn nhất.
c=1
for tong_lon_nhat in duong_lien_tiep:
    if sum(tong_lon_nhat)==tong_max:
        c+=1
print(f"phần tử lớn nhì trong danh sách là: {lon_nhi},số phần tử lớn nhì có trong danh sách là {so_lon_nhi}")
print(f"so luong cac so duong lien tiep nhieu nhat la: {so_sanh}")
print(f"so luong cac so duong lien tiep co tong lon nhat la",c)