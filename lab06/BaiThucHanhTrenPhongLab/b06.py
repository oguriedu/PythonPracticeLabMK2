import random

A = [random.randint(1, 99999) for i in range(1000)]
print(A)

c1 = sorted(A)
print(c1)


c2 = A.copy()
n = len(c2)
for i in range(n):
    for j in range(0, n-i-1):
        if c2[j] > c2[j+1]:
            c2[j], c2[j+1] = c2[j+1], c2[j]
print(c2)
