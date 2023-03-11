a = [2,-4,1,9,-3,6,3,-2,6,8]
sum1 = 0
lstd = []
sum2 = 0

for i in a:
    sum1 += i
    if i > 0:
        lstd.append(i)
        sum2 += i
        z = a.index(i)
    c = max(a)
    v = a.index(c)

for i in a:
    if i < 0:
        a.reverse()
        x = a.index(i)

print("Tong tat ca cac phan tu trong list la:",sum1)
print("So luong cac so duong la:",len(lstd),", Tong cua chung la:",sum2)
print("Vi tri cua phan tu duong cuoi cung la:",z)
print("Vi tri cua phan tu am dau tien la:",x)
print("Phan tu co gia tri lon nha la:",c,", Vi tri cua no la:",v)