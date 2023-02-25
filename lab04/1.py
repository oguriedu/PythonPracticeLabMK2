
s4=0
s5=0
s6=0
n=int(input('nhập số nguyên dương n:'))
i=1
while n<=0:
    n=int(input('nhập số nguyên dương lớn hơn 0:'))
while i<=n:
    s4+=i**2
    s5+=(2*i+1)**3
    s6+=(2*i)**4
    i=i+1
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)
    
    