n = int(input("nhập n:  "))
while n<=0:
    n = int(input(" nhập số nguyên dương: "))
# phân a
S4 = 0
for i in range(1,n+1):
    i = i**2
    S4 = S4 + i
print("tổng giá trị của S4 là: ",S4)
# phần b
S5 = 0
for i in range(1,2*n + 1, 2):
    i = i**3
    S5 = S5 + i
print("tổng giá trị của S5 là: ",S5)
# phần c
S6 = 0
for i in range(2,2*n, 2):
    i = i**4
    S6 = S6 + i
print("tổng giá trị của S6 là: ",S6)
