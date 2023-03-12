#
import random 
a = []
for i in range(1,1001):
    b = random.randint(1,99999)
    a.append(b)
print(sorted(a))