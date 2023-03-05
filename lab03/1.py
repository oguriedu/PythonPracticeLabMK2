n=int(input("nhap n:"))
sum=1
j=1
for i in range(1,n+1):
    sum*=(2*i+1)/(2*i+2)
print(sum)