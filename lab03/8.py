s1=0
s2=0
s3=0
n=int(input('nhập số n:'))
if n<=0:
    n=int(input('mời bạn nhập lại:'))
else:
    for i in range(1,n+1):
        s1=i*(i+1)/2
        s2=(i+1)*2
        s3=i*(i+1)
    print("s1=",s1)
    print("s2=",s2)
    print("s3=",s3)