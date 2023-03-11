#tính toán liên quan đến  list
a=[2,-4,1,9,-3,6,3,-2,6,8]
#tính tổng các phần tử trong list
print("tổng các phần tử trong list là : ",sum(a))
#đếm các số hạng dương
count=0
tong=0
for c in a:
    if c>0:
        count+=1
        tong+=c
print("số các phần tử dương trong danh sách là",count)
#tính tổng các phần tử dương:
print("tổng các phần tử dương trong danh sách là", tong)
#tìm phần tử âm đầu tiên trong dãy là:
for i in a:
    if i<0:
        print("phân tử âm đầu tiên trong dãy là:",i)
        break
#tìm phần tử dương cuối cùng trong dãy
phan_tu_duong_cuoi = []
for i in range(len(a)):
    if a[i] > 0:
        phan_tu_duong_cuoi = i
print("phân tử dương cuối cùng trong dãy nằm ở vị trí thứ : ",phan_tu_duong_cuoi)
#tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuỗi cùng:
phan_tu_lon_nhat = -4
vi_tri_phan_tu_lon_nhat= []

for i in range(len(a)):
    if a[i] >= phan_tu_lon_nhat:
        phan_tu_lon_nhat = a[i]
        vi_tri_phan_tu_lon_nhat = i
print("Phần tử lớn nhất của danh sách là:", phan_tu_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách là:", vi_tri_phan_tu_lon_nhat)
