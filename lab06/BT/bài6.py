import random
list = []

for i in range(1000):
  num = random.randint(1,99999)
  list.append(num)

print(list)
print(len(list))