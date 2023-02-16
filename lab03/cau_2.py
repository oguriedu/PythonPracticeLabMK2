#cau2
#Tim so hoan hao nho hon n
n = int(input("nhap n: "))
list = []
for i in range (1, n):
    sum = 0
    for j in range (1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        list.append(i)
print("cac so hoan hao nho hon n la: ", list)