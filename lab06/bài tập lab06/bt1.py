a =[2,-4,1,9,-3,6,3,-2,6,8]
n =10
#Tính tổng
s =0
for i in a:
    s+=i
print("tổng tất cẩ phần tử trong a",s) 
## Tính tổng số dương
dem =0
tong =0
for i in range(0,n):
    if a[i]>0:
        dem+=1
        tong+=a[i]
print("số hạng dương có:",dem,"số")       
print("Tổng số dương trong a:",tong)
#Tìm phần tử âm đầu tiên trong ds
for i in a:
    if a[i]<0:
      print("số hạng âm đầu tiên là ",a[i])
      break
print("số hạng âm đầu tiên là số có vị trí:",i+1)
#Tìm phần tử dương cuối cùng trong ds
j=n-1
while a[j]<=0:
    j=1
    if j==-1:
        break
if j==-1:
    print("ko có phần tử dương")
else:
    print("vị trí của phần tử dương cuối cùng là:",j+1)
# phần tử lớn nhất vs vị trí của nó
lst =[]
for i in range(0,n):
    if a[i]==max(a):
        lst.append(i)
print(f"Phần tử lớn nhất trong danh sách là {max(a)}")
print(f"vị trí của phần tử lớn nhất cuối cùng là {lst[-1]} ")