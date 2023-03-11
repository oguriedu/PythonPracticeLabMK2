j1 = []
j2 = []
j = []
while True:
    a = int(input("nhập số: "))
    j.append(a)
    if a == 0:
        break

for i in j:
    if i > 0:
        j1.append(i)
    if i < 0:
        j2.append(i)
j3 = j1 + j2
print(j3)

m = int(input("nhập phần tử muốn thêm vào: "))
j.reverse()
j.append(m)
j.reverse()
j.append(m)
print(j)
a = []
for i in j:
    if i == j[5]:
        a.append(m)
    a.append(i)
print(a)