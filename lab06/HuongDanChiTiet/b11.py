n = int(input("Nhap vao bac cua ma tran don vi: "))
A = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    A[i][i] = 1
print("Ma tran don vi bậc", n, "la:")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
