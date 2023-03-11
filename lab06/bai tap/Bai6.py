import random
A = []
for i in range(1000):
    A.append(random.randint(1, 99999))
print(A)
#thu tu cach 1
A.sort()
print("Thu tu tang dan: ",A)
#thu tu cach 2
def bubble_sort(A):
    n = len(A)
   
    for i in range(n - 1):
        # Lặp lại từng cặp phần tử
        for j in range(0, n - i - 1):
            # So sánh và hoán đổi nếu cần thiết
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

bubble_sort(A)
print("Thu tu tang dan: ",A)

