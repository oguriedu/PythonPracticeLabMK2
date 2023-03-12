n=10
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
for i in range(0,n): print(a[i],' ',end='')
print()

# Tính tổng các phần tử của danh sách
tong=0
for i in range(0,n):tong+=a[i]
print('Tổng =',tong)

#Đếm số lượng các số hạng dương và tổng của các số hạng dương
dem= 0
tongdem= 0 
for i in range (0, n):
    if a[i]> 0:
        dem+= 1
        tongdem+= a[i]
print ("số hạng dương là:", dem)
print ("tổng các số hạng dương là:", tongdem)

#Tìm vị trí phần tử âm đầu tiên trong danh sách
i=0
while a[i]>= 0:
    i+= 1
    if i== n:
        break
if i== n:
    print ("không có phần tử âm")
else:
    print ("vị trí của phần tử âm đầu tiên là:", i+1)

#Tìm vị trí phần tử dương cuối cùng trong danh sách
i=n-1
while a[i] <=0:
    i-=1
    if i==-1:
        break
if i==-1:
    print ("không có phần tử dương")
else:
    print ("vị trí phần tử dương cuối cùng là:", i+1) 

# Tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuối cùng
max=a[0]
vt=0
for i in range(1,n-1):
    if a[i]>max:
        max=a[i]
        vt=print('Số lớn nhất là',max,'tại vị trí',vt+1) 