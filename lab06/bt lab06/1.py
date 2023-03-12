n=10
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
for i in range(0,n): print(a[i],' ',end='')
print()
#Tính tổng các phần tử của danh sách
tong=0
for i in range(0,n):tong+=a[i]
print('Tổng =',tong)
#Đếm số hạng dương và tổng các số dương
dem=0
tongd=0
for i in range(0,n):
    if a[i]>0:
       dem+=1
       tongd+=a[i]
print('Số hạng dương:',dem)
print('Tổng số dương:',tongd)

#Tìm vị trí phần tử âm đầu tiên trong danh sách
i=0
while a[i]>=0:
    i+=1
    if i==n:
       break
if i==n:
    print('Không có phần tử âm')
else:
    print('Vị trí phần tử âm đầu tiên:',i+1)
#Tìm vị trí phần tử dương cuối cùng trong danh sách
i=n-1
while a[i]<=0:
   i-=1
   if i==-1:
      break
if i==-1:
    print('Không có phần tử dương')
else:
    print('Vị trí phần tử dương cuối cùng:',i+1)
#Tìm phần tử lớn nhất và vị trí của phần tử lớn nhất cuối cùng
max=a[0]
vt=0
for i in range(1,n-1):
    if a[i]>max:
        max=a[i]
        vt=i
print('Số lớn nhất là',max,'tại vị trí',vt+1)