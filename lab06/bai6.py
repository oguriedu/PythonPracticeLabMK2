import random
A = []
for i in range(100):
    A.append(random.randint(1,99999))
print(A)

A1 = A.copy()
A1.sort()
print('Sử dụng sort():',A1)

A2 = A.copy()
for i in range(len(A2)):
    for j in range(i+1):
        if A2[i] < A2[j]:
            tg = A2[i]
            A2[i] = A2[j] 
            A2[j] = tg
print('Không sử dụng sort():',A2)

