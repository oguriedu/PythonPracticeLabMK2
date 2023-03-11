from random import randint
a = []
for i in range(1,1001):
    b = randint(1,99999)
    a.append(b)
a.sort()
print(a)