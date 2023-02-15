n=int(input('Nhập n: '))
print('Số nguyên tố nhỏ hơn hoặc bằng n là: ',end='')
for i in range(1,n+1):
    check=True
    if (i<2):
        continue
    for j in range(2,i):
        if (i % j == 0):
           check = False
    if check == False:
        continue
    print(i,end=' ')