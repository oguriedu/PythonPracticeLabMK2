a=[]
while True:
    n=int(input('Nhập phần tử của list( Nhập 0 để dừng): '))
    if n==0:
        break
    a.append(n)
b=[1,2,3]
list1=[]
list2=[]
for i in range(0,5):
    list1.append(a[i])
for i in range(5,len(a)):
    list2.append(a[i])
kq=[]
kq.extend(b)
kq.extend(list1)
kq.extend(b)
kq.extend(list2)
kq.extend(b)
print('Danh sách sau khi chèn: ',kq)
k=int(input('Nhập vị trí cần xoá: '))
kq.pop(k)
print('Danh sách sau khi xoá: ',kq)
kq.sort()
print('Sắp xếp tăng:',kq)
kq.reverse()
print('Sắp xếp giảm:',kq)
