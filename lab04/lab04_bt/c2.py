import math
n=int(input("Nhập n: "))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    s1+=(-1/(i*math.pow(-1,i)))
    s2+=(1/i)*(1/(i+1))
    s3+=(1/(math.sqrt(i+1)))
    i+=1
print(s1,s2,s3)