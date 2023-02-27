n = int(input("Nhap n: "))
if n<=0:
  n = int(input("Nhap n lai: "))

s= 0
#
for i in range(1, n+1):
  s+= i**2
  
print("S4 = 12 + 22 + 32 + ... + n2 =", s)
#
for i in range(1,n+1,2):
    if i%2!=0:
        s+=i**3
print("S5 = 1^3 + 3^3 + 5^3 + … + (2n+1)^3 =",s)        
