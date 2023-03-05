n=int(input('Nhập hệ 10: '))
a=0
b=[]
while True:
    a=n%2
    n=n//2
    b.append(a)
    if n==0:
        break
c=b[::-1]
print('Chuyển từ hệ 10 sang hệ 2 là: ',end='')
for i in c:
    print(i,end='')