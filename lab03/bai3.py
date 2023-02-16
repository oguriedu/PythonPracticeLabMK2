n=int(input('nhập n:'))
print('các số nguyên tố bé hơn hoặc bằng',n,'là:')
for i in range(2,n+1):
    if i>=2:
        for j in range(2,i):
            if (i%j)==0:
                break
            else:
                print(i,end=',')