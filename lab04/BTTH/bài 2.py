#Phần a
i=1; s=0
while True:
    s=s+((-1)**(i+1))/i
    i+=1
    if i==10000:
        print(s)
        break

#Phần b
i=1; s=0
while True:
    s=s+1/(i*(i+1))
    i+=1
    if i==10000:
        print(s)
        break

#Phần c
import math
i=1; s=0
while True:
    s=s+1/math.sqrt(i)
    i+=1
    if i==10000:
        print(s)
        break