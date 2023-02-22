n=int(input("Nhập n (là số nguyên dương): "))
while n<=0:
    n=int(input("Mời bạn nhập lại n: "))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    s1+=i
    s2+=(2*i+1)
    s3+=2*i
    i+=1
print("S1 =",s1 ,"\n","S2 =",s2,"\n","S3 =",s3,"\n")