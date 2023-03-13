m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []
for i in range(m):
    row = []
    for j in range(n):
        aij = int(input(f"Nhập giá trị a{i+1}{j+1}: "))
        row.append(aij)
    A.append(row)

total = 0
for i in range(m):
    for j in range(n):
        total += A[i][j]

print(f"Tổng các phần tử của ma trận A là {total}")
