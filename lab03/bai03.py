n=int(input('Nhập n = '))
so_uoc=0
for i in range(1,n+1):
    if n%i==0:
        so_uoc+=1
if so_uoc==2:
   print(n,'là số nguyên tố')
else:
    print(n,'không là số nguyên tố')
    for i in range(1,n+1):
        so_uoc=0
        for j in range(1,i+1):
            if i%j==0:
                so_uoc+=1
        if so_uoc==2 :
            max=2 #Số nguyên tố nhỏ nhất là 2
            if i>max:
                max=i
    print('Số nguyên tố gần n nhất là :',max)

