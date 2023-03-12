import random
a = []
for i in range(1, 99999):
    a.append(i)
A = random.choices(a, k=1000)
A1 = random.choices(a, k=1000)
#sort function
A.sort()
print('list A =', A)
#algorithm
for j in range(1, len(A1)):
    key = A1[j]
    k = j-1
    while k >= 0 and A1[k] > key:
        A1[k+1] = A1[k]
        k -= 1
    A1[k+1] = key
print('list A1 =', A1)