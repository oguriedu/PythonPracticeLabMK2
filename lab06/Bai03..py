a=[]
while True:
    n=int(input('Nhập phần tử của list( Nhập 0 để dừng ): '))
    if n==0:
        break
    a.append(n)
duong=[]
am=[]
for i in a:
    if i>0:
        duong.append(i)
    else:
        am.append(i)
duong.extend(am)
print('Danh sách sau khi chuyển số dương lên đầu: ',duong)
m=int(input('Nhập số cần chèn: '))
a.insert(0,m)
a.append(m)
a.insert(5,m)
print(a)
    


