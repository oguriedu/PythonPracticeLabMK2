j = []
n = int(input("nhập số lượng phần tử: "))
for i in range(1, n+1):
    a = int(input("nhập số tự nhiên: "))
    j.append(a)
a1 = j.copy()
print(j)
a1.sort()
a1.remove(max(a1))
s1 = 0
for i in j:
    if i == max(a1):
        break
    s1 += 1
print("phần tử lớn thứ nhì là: ",max(a1))
print("nằm ở vị trí thứ: ", s1 + 1)
# phần b
def list(x):
    s1 = 0
    a1 = []
    for i in x:
        if i >= 0:
            continue
        else:
            a1.append(i)
        s1 += 1
    else:
        print("vòng lặp đc thực thi hết")