import random
A = []
for i in range(1000):
    A.append(random.randint(1,99999))
#dùng sorted
A_sorted = sorted(A,reverse=False)
print(A_sorted)
#không dùng sorted
for i in range(1, len(A)):
    j = i - 1
    key = A[i]
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
print(A)