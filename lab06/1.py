#tính tổng các phần tử
n=10
a=[2,-4,1,9,-3,6,3,-2,6,8]
tong = 0
for i in range(0,n):
    a.append(n)
    tong += a[i]
print('Tổng các phần tử là: ',tong)
#đếm các số hạng dương và tính tổng các số hạng dương 
dem = 0
tongd = 0
for i in range(0,n):
    if a[i]>0:
        dem += 1
        tongd += a[i]
print("Số hạng dương là: ",dem)
print("Tổng số hạng dương là: ",tongd)

#tìm vị trí của phần tử âm đầu tiên
i=0
while a[i]>=0:
    i+=1
    if i==n:
        break
if i==n:
    print("Không có phần tử âm")
else:
    print("Vị trí phần tử âm đầu tiên là: ",i+1)

#Tìm vị trí của phần tử dương cuối cùng trong danh sách
d=n-1
while a[d]<=0:
    d=1
    if d==-1:
        break
if d==-1:
    print("Không có phần tử dương")
else:
    print("Vị trí phần tử dương cuối cùng là: ",d+1)

#Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
ptln=a[0]
vitri=0
for p in range(1,n-1):
    if a[p]>ptln:
        ptln=a[p]
        vitri=p
print("Phần tử lớn nhất của danh sách là: ",ptln,"Vị trí của phần tử lớn nhất cuối cùng là: ",vitri+1)