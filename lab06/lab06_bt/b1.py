n=10
a=[2,-4,1,9,-3,6,3,-2,6,8]
# ý1
sum=0
for i in a:
    sum+=i
print('Tổng các phần tử trong a là:',sum)
#ý2
count=0
sum1=0
for i in a:
    if i>0:
        count+=1
        sum1+=i
print('Tổng các phần tử dương trong a là:' ,sum1)
print('Số hạng dương trong phần tử a là:',count)
#Ý3
for i in a:
    if i<0:
        print(f"Vị trí phần tử âm đầu tiên là: {a.index(i)+1}")
        break
#Ý4
for i in a:
  if a[i]>0:
        print(f"Vị trí phần từ dương cuối cùng là {a.index(a[i])+1}")
        break
#ý5
max=a[0]
vt=0
for i in a:
    if a[i]>max:
        max=a[i]
        vt=i
print('Số lớn nhất là',max,'tại vị trí',vt+1)

