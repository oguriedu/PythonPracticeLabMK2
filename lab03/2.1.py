n = int(input("Nhập số nguyên dương: "))

while n <= 0:
  print("Nhập lại số nguyên dương")
  n = int(input("Nhập số nguyên dương: "))
  
s = 0
# 1
for i in range(1, n+1):
  s += i
  
print("S1 = 1 + 2 + 3 + ... + n =", s)
print("S1 = n(n+1)/2 =", n*(n+1)/2)
#2
for i in range(1,n+1):
  if i%2!=0:
   s+=(2*i+1)
  
print("S2 = 1 + 3 + 5 + … + (2n+1) =",s)
print("S2 = (n+1)2 =",(n+1)**2)  
#3
for i in range(2,2*n+2,2):
  if i%2==0:
    s+=i
print("S3 = 2 + 4 + 6 + … + 2n =",s)
print("S3 = n(n+1)",n*(n+1))  
