import random
list = []

for i in range(1000):
  num = random.randint(1,99999)
  list.append(num)

print(list)
print(len(list))

list.sort(reverse=False)
print("Sap xep tang dan khi dung sort:",list)

n = len(list)

for i in range(n):
    for j in range(0, n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)