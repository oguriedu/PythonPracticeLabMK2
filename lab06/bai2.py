def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])

    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]
    return max_2
n = int(input("Nhap vao so phan tu cua danh sach: "))
print("Nhap vao danh sach:")
a = []
for i in range(n):
    print("\tPhan tu thu", i+1,"la:", end=" ")
    a.append(int(input()))

print("Danh sach vua nhap la:")
for i in range(n):
    print("\t", a[i], end="")

print("\nPhan tu lon thu hai trong danh sach tren la:", Find_max_second(a))
for i in range(len(a)):
        if a[i]==Find_max_second(a):
            print(i+1,end=", ")
print(end="")
###
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
print("tổng dãy số dương",sum(a))