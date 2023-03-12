a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong=0
duong=0
am=0
lon_nhat=0
so_duong=0

for i in a:
    tong+=i
    if i>0:
        duong+=i
        so_duong+=1
    if i>lon_nhat:
        lon_nhat=i
lon_cuoi=a.index(lon_nhat)
for j in a:
    if j<0:
        am+=j
        break
vi_tri_am=a.index(am)
for cuoi in a:
    if cuoi>0:
        phan_tu_cuoi=a.index(cuoi)
print(f"tong cac phan tu trong danh sach la : {tong}")
print(f"tong cac so hang duong la : {duong}, so luong cac so hang duong la: {so_duong}")
print(f"vi tri phan tu am dau tien trong danh sach la: {vi_tri_am}")
print(f"vi tri phan tu duong cuoi cung trong danh sach la: {phan_tu_cuoi}")
print(f"phan tu lon nhat cua danh sach la {lon_nhat},vi tri phan tu lon nhat cuoi cung la: {lon_cuoi}")
