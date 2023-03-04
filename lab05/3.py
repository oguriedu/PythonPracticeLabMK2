def dec2bin(n):
    k=[]
    while(n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    kq=''
    k.reverse()
    #chuyen doi list sang string
    for i in k:
        kq+=str(i)
    return kq
n=int(input('nhập số:'))
print('so',n,"có dạng nhị phân là",dec2bin(n))