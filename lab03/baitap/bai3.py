n=int(input("nhap so duong n: "))
if n<2:
    print(f"{n} khong phai so nguyen to")
if n == 1 or n == 0  :
    print('so nguyen to gan nhat la 2')
flag=True
for i in range (2,n,1):
    if n%i==0:
        flag=False
        print(f"{n} khong phai so nguyen to")
        break
else:
    print(f"{n} la so nguyen to")

if flag==False:
    for i in range(n-1,2,-1):
        for j in range(2,i,1):
            if i % j ==0:
                break
        else:
            print(f"{i} la so nguyen to gan nhat ben trai")
            break
else:
    print(f"khong co so nguyen to nao ben trai {n}")
for i in range(n+1,10000000,1):
    for j in range(2,i,1):
        if i%j==0:
            break
    else:
        print(f"{i} la so nguyen to gan nhat ben phai")
        break
else:
    print(f" khong co so nguyen to ben phai{n}")

