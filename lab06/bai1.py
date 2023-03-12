n=10
sum=0
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
for i in range(0,n): 
    print(a[i],' ',end='')
print()
for i in range(0,n):
    sum+=a[i]
print(f'tổng = {sum}')
#dem so luong cac so hang duong vaf tong so
count=0
sumd=0
for i in range(0,n):
    if a[i]>0:
        count+=1
        sumd+=a[i]
print(f'số hạng dương là {count}')
print(f'tổng các số hạng dương là {sumd}')
#tim vi trí phần tử âm trong danh sách
i=0
while a[i]>=0:
    i+=1
    if i==n:
       break
if i==n:
    print('Không có phần tử âm')
else:
    i=n-1
while a[i]<=0:
    i-=1
    if i==-1:
        break
if i>-1:
    print('vị trí',i+1)