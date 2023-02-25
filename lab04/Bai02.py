import math
sa=0
sb=0
sc=0
while True :
    n=int(input('Nhập n = '))
    if n>0:
        i=1
        while i<=n:
            a=(-((-1)**i))*1/i
            sa+=a
            sb+=1/(i*(i+1))
            sc+=1/math.sqrt(i+1)
            i+=1
        print('Sa = ',sa)
        print('Sb = ',sb)
        print('Sc = ',sc)
        break
        