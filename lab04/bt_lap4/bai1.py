n=int(input('nhập giá trị n:'))
s=0
s2=0
s3=0
if n<=0:
    print('Bạn nhập sai yc bài, mời bạn nhập lại')
else:
    for i in range(n+1):
        s+=i**2
    print('Gía trị biểu thức:',s)
    for i in range(1,2*n+2,2):
        s2+=i**3
    print('Gía trị của biểu thức:',s2)
    for i in range(2,2*n+1,2):
        s3+=i**4
    print('Gía trị của biểu thức là:',s3)
    
