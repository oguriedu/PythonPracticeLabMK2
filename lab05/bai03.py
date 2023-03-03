n=int(input('Nhập hệ 10: '))
a=0
c=[]
while True:
    a=n%2
    n=n//2
    c.append(a)
    if n==0:
        break
c1=c[::-1]
print('Chuyển từ hệ 10 sang hệ 2 là: ',end='')
for i in c1:
    print(i,end='')