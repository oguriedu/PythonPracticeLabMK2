n=int(input("moi nhap n: "))
tong=0
if n<=0:
    print('moi ban nhap lai')
else:
    for i in range(0,n):
        i+=1
        tong+=i
print(tong)
