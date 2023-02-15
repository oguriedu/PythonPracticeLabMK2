n=int(input('Nhập n = '))
print('Số nguyên tố nhỏ hơn hoặc bằng n là :')
for i in range(1,n+1):
    so_uoc=0
    for j in range(1,i+1):
        if i%j==0:
            so_uoc+=1
    if so_uoc==2 :
        print(i,end=' ')