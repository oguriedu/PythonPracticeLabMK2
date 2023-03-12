import random
a = []
for i in range(1, 99999):
    a.append(i)
A = random.choices(a, k=1000)
# in ds A gồm 1000 số tự nhiên
print (A)