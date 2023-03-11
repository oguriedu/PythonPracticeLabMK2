j = []
a = [1, 2, 3]
while True:
    a1 = int(input("nhập số: "))
    j.append(a1)
    if a1 == 0:
        break
print(j)
for i in a:
    j.append(i)
j.reverse()
a.reverse()
for i in a:
    j.append(i)
j.reverse()
print(j)
k = int(input("nhập vị trí bạn muốn xóa: "))
j.remove(k)
print(j)
j.sort()
# tăng dần
print(j)
# giảm dần
j.reverse()
print(j)