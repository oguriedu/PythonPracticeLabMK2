import random

A = [random.randint(1, 99999) for _ in range(1000)]

# Sử dụng hàm sorted()
A_sorted_1 = sorted(A)
print(A_sorted_1)

# Không sử dụng hàm sorted()
n = len(A)
for i in range(n):
    for j in range(0, n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

A_sorted_2 = A

# Kiểm tra
assert all(A_sorted_1[i] == A_sorted_2[i] for i in range(len(A)))
assert all(A_sorted_1[i] <= A_sorted_1[i+1] for i in range(len(A_sorted_1)-1))
assert all(A_sorted_2[i] <= A_sorted_2[i+1] for i in range(len(A_sorted_2)-1))
print(A_sorted_2)
