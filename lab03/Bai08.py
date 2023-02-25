n=int(input('Nhập n = '))
while n<=0:
    print('Mời nhập lại n>0 !')
    n=int(input('Nhập n = '))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    s1+=i
    s3+=2*i
for i in range(0,n+1):
    s2+=2*i+1
print('S1 = ',s1)
print('S2 = ',s2)
print('S3 = ',s3)