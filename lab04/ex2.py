import math
n=int(input("Nhập số:"))
ex =0
for a in range(1,n+1):
    if a%2==0:
        ex -= 1/a
    else:
        ex +=1/a
print(ex)
sum = 0
for i in range(2,n+1):
    sum += 1/math.sqrt(i)
print(sum)
