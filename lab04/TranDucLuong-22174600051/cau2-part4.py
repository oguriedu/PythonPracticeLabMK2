n=int(input('n='))
import math 
suma=0
sumb=0
sumc=0
i=1
for i in range (2,n+1):
    C=1/math.sqrt(i)
    B=1/((i-1)*i)
    sumb+=B
print(sumb)
