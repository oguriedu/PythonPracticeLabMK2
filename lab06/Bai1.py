a=[2,-4,1,9,-3,6,3,-2,6,8]
n=10
#tính tổng
b=sum(a)
print(b)
#đếm số lượng và tính tổng
count = 0
sum=0
for num in a:
    if num > 0:
        count += 1
        sum += num

print("Số lượng số dương trong danh sách là:", count)
print("Tổng các số dương: ",sum)
#tìm vị trí phần tử số âm đầu tiên trong danh sách
i=0
while a[i]>=0:
    i+=1
    if i==n:
       break
if i==n:
    print('Không có phần tử âm')
else:
    print('Vị trí phần tử âm đầu tiên:',i+1)
#Tìm vị trí của phần tử dương cuối cùng trong danh sách
i=n-1
while a[i]<=0:
   i-=1
   if i==-1:
      break
if i==-1:
    print('Không có phần tử dương')
else:
    print('Vị trí phần tử dương cuối cùng:',i+1)
#Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
max=a[0]
vt=0
for i in range(1,n-1):
    if a[i]>max:
        max=a[i]
        vt=i
print('Số lớn nhất là',max,'tại vị trí',vt+1)
