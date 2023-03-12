n=int(input("so phan tu cua list a:"))
import random
import math
listA=[]

for i in range(1,n+1):
    b=int(input("nhaap so trong list a :"))
    listA.append(b)
print(listA)
listB=[y%3==0 and y%5==0 for y in listA]
print(listB)
listC=[z**2 for z in listA]
print(listC)
listD=random.choice(listA)
print([listD])

