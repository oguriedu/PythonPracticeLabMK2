a=[]
while True:
    nhap=[]
    name=input("mời nhập tên: ")
    age=int(input("mời nhập tuổi: "))
    height=float(input("mời nhập chiều cao: "))
    nhap.append(name)
    nhap.append(age)
    nhap.append(height)
    nhap=tuple(nhap)
    a.append(nhap)
    tiep=int(input("bạn có muốn tiếp tục? 1:có"))
    if tiep != 1:
        break
for i in range(len(a)):
    for j in range(i):
        if len(a[i][0])<len(a[j][0]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)