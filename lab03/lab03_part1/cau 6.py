import math
sum=0
n=int(input("Nhập n: "))
for i in range(1,n+1):
    sum+=math.pow(i,3)
    i+=1
print("%i"%sum)