n = 0
while n <= 0:
    n = int(input("Nhập số nguyên dương n: "))

S1 = 0
for i in range(1, n+1):
    S1 += i

S2 = 0
for i in range(1, 2*n+2, 2):
    S2 += i

S3 = 0
for i in range(2, 2*n+1, 2):
    S3 += i

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
