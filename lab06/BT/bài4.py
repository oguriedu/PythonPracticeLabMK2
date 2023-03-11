import random
a = []

for i in range(1000):
  num = random.randint(1,99999)
  a.append(num)

print(a)
print(len(a))