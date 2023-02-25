n=int(input('Nhập n = '))
for i in range(1,n+1):
    so_uoc=0
    for j in range(1,i+1):
        if i%j==0:
            so_uoc+=1
    if so_uoc==2 : 
        if n%i==0:
            a=0
            while n%i==0:
                a+=1
                n//=i
            print((str(i)+'^'+str(a)),end='*')