n = int(input("Nhập số phần tử của dãy số : "))
a = [int(input(">>")) for i in range(n)]
print(a)
#Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
B=a.copy()
m=max(B)
i=0
while i<len(B):
    if B[i]==m:
        B.remove(B[i])
        i-=1
    i+=1
if len(B)==0:
    print("Khong co so lon nhi")
else:
    m=max(B)
    print("So lon nhi la",m,"tai vi tri",end=" ")
    for i in range(len(a)):
        if a[i]==m:
            print(i+1,end=", ")
#Số lượng các số dương liên tiếp nhiều nhất
d=len(a)
i=0
maxd=0
while i<d:
    while a[i]<=0:
        i+=1
        if i==d:break
    if i<d:
        max1=0
        j=i
        while a[j]>0:
            max1+=1
            j+=1
            if j==d: break
        if max1>maxd: 
            maxd=max1
        i=j
    i+=1
print('So duong lien tiep dai nhat =',maxd)
#Tổng số dương liên tiếp lớn nhất
d=len(a)
i=0
sumd=0
while i<d:
    while a[i]<=0:
        i+=1
        if i==d:break
    if i<d:
        sum1=0
        j=i
        while a[j]>0:
            sum1+=a[j]
            j+=1
            if j==d: break
        if sum1>sumd: 
            sumd=sum1
        i=j
    i+=1
print('Tong so duong lien tiep dai nhat =',sumd)