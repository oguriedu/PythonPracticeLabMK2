import random
a = []
for i in range(1000):
    number = random.randint(1,99999)
    a.append(number)
'day so tu nhien random'
b=a.copy()
a.sort()
print('Sap xep dung ham sort:',a)
for i in range(len(b)):
    for j in range(len(b)-i-1):
        if b[j] > b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print('ko su dung ham sort:',b)