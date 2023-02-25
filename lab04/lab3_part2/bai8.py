n = int(input('nhập n'))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    if n<=0:
        print('bạn vui lòng nhập lại')
        n = int(input('nhập n'))
    if n>0:
        s1+=n*(n+1)/2
        s2+=(n+1)*2
        s3+=n*(n+1)
        n=n+1
    print('s1=',s1)
    print('s2=',s2)
    print('s3=',s3)
    break
