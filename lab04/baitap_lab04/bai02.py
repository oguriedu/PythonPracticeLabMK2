import math
n = int(input("nhập n = "))
s = 0
i = 0
a = 1
k = 0
j = 0
while i < n:
    i += 1
    s += a*1/i
    a *= -1
    k += 1/((i+1)*i)
    j += 1/(math.sqrt(i+1))
print("a, Tổng chuỗi S = {:.2f}".format(s))
print("b, Tổng chuỗi S = {:.2f}".format(k))
print("c, Tổng chuỗi s = {:.2f}".format(j))