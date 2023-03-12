a=[-2,4,1,9,-3,6,3,-2,6,8]
print('Tổng các phần tử trong danh sách là:',sum(a))
b=[]
c=10
for i in a:
    if i>=0:
        b.append(i)
print('Số lượng các số hạng dương là:',len(b))
print('Tổng các số hạng dương là:',sum(b))
i=0
while a[i]>=0:
    i+=1
    if i==c:
       break
if i==c:
    print('Không có phần tử âm')
else:
    print('Vị trí phần tử âm đầu tiên:',i+1)
i=c-1
while a[i]<=0:
   i-=1
   if i==-1:
      break
if i==-1:
    print('Không có phần tử dương')
else:
    print('Vị trí phần tử dương cuối cùng:',i+1)
max=a[0]
vt=0
for i in range(1,c-1):
    if a[i]>max:
        max=a[i]
        vt=i
print('Số lớn nhất là',max,'tại vị trí',vt+1)