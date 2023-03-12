b=int(input("nhập số  : "))
for m in range(1,b+1):
    h=0
    for i in range(1,m):     
        if (m%i==0):
            h=h+i
    if h==m:
        print(m,"là số hoàn hẻo")