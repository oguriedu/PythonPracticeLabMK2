# Nhập vào số phần tử của danh sách
n = int(input("Nhập số phần tử của danh sách: "))

# Khởi tạo một danh sách các số tự nhiên có n phần tử
lst = []
for i in range(n):
    x = int(input("Nhập phần tử thứ {} của danh sách: ".format(i+1)))
    lst.append(x)

# Tìm phần tử lớn thứ nhì của danh sách
max1 = max(lst)
lst.remove(max1)
max2 = max(lst)
vt_max=0
print("Phần tử lớn thứ nhì của danh sách là:", max2)
#tìm số lượng số dương và tổng dãy số dương
for i in range(len(lst)):
        if lst[i]==max1:
            print(i+1,end=", ")
print(end="")
a=len(lst)
i=0
maxd=0
while i<a:
    while lst[i]<=0:
        i+=1
        if i==a:break
    if i<a:
        max1=0
        j=i
        while lst[j]>0:
            max1+=1
            j+=1
            if j==a: break
        if max1>maxd: 
            maxd=max1
        i=j
    i+=1
print('số lượng số dương liên tiếp  =',maxd)
print("tổng dãy số dương = ",sum(lst))
