import random
a = []
for i in range(1000):
    a.append(random.randint(1,99999))
a_sorted = sorted(a,reverse=False)
print(a_sorted)
for i in range(1, len(a)):
    j = i - 1
    key = a[i]
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
print(a)