n = int(input("Nhập n: "))
if n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

S1 = n * (n + 1) // 2
S2 = (n + 1) ** 2
S3 = n * (n + 1)

print("S1 = ", S1)
print("S2 = ", S2)
print("S3 = ", S3)
