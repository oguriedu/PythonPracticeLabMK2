#viết chương trình tính tổng bậc 3 của n số nguyên đầu tiên
n = int(input("nhập số n: "))
b = 0
for i in range(1, n+1):
    a = i**3
    b += a
print(b)