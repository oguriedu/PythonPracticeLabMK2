n=int(input('moi so nguyen duong n: '))
flag=True
if n<2:
    print(f'khong the phan tich thanh thua so nguyen to cua {n}')
so_nguyen_to=[]
for i in range(2,n):
    if n % i == 0:
        flag=False
        break
else:
    flag = True
    print(f'{n} không phải thể phân tích thành thừa số nguyên tố')
a=0
b=n
if flag==False:
    for j in range(2,n):
        if b%j==0:
            a+=j
            for k in range(2,a+1):
                if a%k==0:
                    so_nguyen_to.append(k)                                        
            b/=j
            a*=0
tich=[]
for q in so_nguyen_to:
    chia=n%q
    if chia==0:
        tich.append(q)
        n/=q
        chia=n%q
        if chia==0:
            for m in range(1,int(n)):
                tich.append(q)
                n/=q
                chia=n%q
                if chia!=0:
                    break
in_ra=""
for chuoi in tich:
    in_ra +=str(chuoi)
    in_ra+="x"
    
print("tich thua so nguyen to la: ",in_ra)
