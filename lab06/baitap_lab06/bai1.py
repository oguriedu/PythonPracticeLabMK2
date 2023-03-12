n=10
a=[2,-4,1,9,-3,6,3,-2,6,8]
#tính tổng
print("Tổng của list trên = ",sum(a))
# đếm số hạng dương và tổng các số dương
dem=0
sum=0
for i in range(0,n):
    if a[i]>0:
        dem+=1
        sum+=a[i]
    print("Số hạng dương ",dem)
    print("Tổng số dương",sum)
#tìm vị trí phần tử âm đầu tiên
i=0
while a[i]>=0:
    i+=1
    if i==n:
       break
if i==n:
    print('Không có phần tử âm')
else:
    print('Vị trí phần tử âm đầu tiên:',i+1)
#tìm vị trí phần tử dương cuối cùng
i=n-1
while a[i]<=0:
   i-=1
   if i==-1:
      break
if i==-1:
    print('Không có phần tử dương')
else:
    print('Vị trí phần tử dương cuối cùng:',i+1)
#tìm phần tử lớn nhất và vị trí cuối cùng
max=a[0]
vt=0
for i in range(1,n-1):
    if a[i]>max:
        max=a[i]
        vt=i
print('Số lớn nhất là',max,'tại vị trí',vt+1)