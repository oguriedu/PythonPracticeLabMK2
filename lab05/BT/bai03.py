n=int(input("nhap n : "))
a=0
b=[]
while True:
    a=n%2
    n=n//2
    b.append(a)
    if n==0:
        break
c1=b[::-1]
print('Chuyển từ hệ 10 sang hệ 2 là: ',end='')
for i in c1:
    print(i,end='')