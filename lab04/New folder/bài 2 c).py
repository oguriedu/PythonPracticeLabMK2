import math
i=1; s=0
while True:
    s=s+1/math.sqrt(i)
    i+=1
    if i==10000:
        print(s)
        break