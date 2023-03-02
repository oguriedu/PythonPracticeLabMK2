import math
n=int(input("nhập n: "))
s4=0
s5=0
s6=0
i=0
while n<=0:
        n=int(input("Nhập lại n: "))
while i<=n:
    
    s4+=math.pow(i,2)
    s5+=math.pow((2*i+1),3)
    s6+=math.pow(2*i,4)
    i+=1
    
print(int(s4),int(s5),int(s6))