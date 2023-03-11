a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
n=10
print("Tổng : ",sum(a))
dem=0
tongd=0
for i in a:
    if a[i]>1:
        dem+=1
        tongd+=a[i]
print("số dương :",dem)
print("tổng số dương:",tongd)
i=0
while a[i]>=0:
    i+=1
    if i==n:
        break
if i==n:
    print("không có phần tử âm :")
else:
    print("phần tử âm đầu tiên :",i+1)
i=n-1
while a[i]<=1:
    i-=1
    if i==-1:
        break
if i==-1:
    print("không có phần tử dương :")
else:
    print("phần tử dương cuối cùng :",i+1)
print("gtln",max(a))
max=a[0]
b=0
for i in range(1,n-1):
    if a[i]>max:
        max=a[i]
        b=i
print('Số lớn nhất là',max,'tại vị trí',b+1)