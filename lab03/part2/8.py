n= int(input("nhập số nguyên dương:"))
while n<=0:
    print ("nhập lại số nguyên dương:")
    break

s=0
for i in range (1, n+1):
    s+=i
    print("kết quả S1 là:", n*(n+1)/2)
    
for i in range (1, n+1):
    if i%2!=0:
        s+=(2*i+1)
        print("kết quả S2 là :", (n+1)**2)
      
for i in range(2,2*n+2,2):
  if i%2==0:
    s+=i
    print("kết quả S3 là:", n*(n+1))