n=int(input('n='))
i=1
sum1=0
sum2=0
sum3=0
import math 
while i<=n:
    a=math.pow(i,2)
    b=math.pow(2*i+1,3) 
    c=math.pow(2*i,4)
    sum1+=a
    sum2+=b
    sum3+=c
    i+=1
print(sum1)
print(sum2)
print(sum3)    