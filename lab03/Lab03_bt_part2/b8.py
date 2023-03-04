n=int(input('Nhập n :'))
while n<=0:
    print('Nhập sai .Mời nhập lại n>0')
    n=int(input('Nhập n: '))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    k1=(i*(i+1))/2
    k2=(i+1)*3
    k3=i*(i+1)
    s1+=k1
    s3+=k2
    s2+=k3
print('tổng S1 là ',s1)
print('tổng S2 là',s2)
print('tổng S3 là ',s3)