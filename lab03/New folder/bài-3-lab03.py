# kiểm tra số nguyên tố
def a(n):
    for i in range(2,n):
        b='không'
        if n%i!=0: b=''
        elif n%i==0: 
            break
    if b=='':print(n,'là số nguyên tố')
    if b=='không':
        j=2;c=[];d=-1
        while j>=2:
            j=j+1
            for i in range(2,j):
                b='không'
                if j%i!=0: b=''
                elif j%i==0: 
                    break
            if b=='': c.append(j); d=d+1
            if c[d]>n: break
        e=abs(n-c[d])
        f=abs(n-c[d-1])
        if f>e: print(n,'không là số nguyên tố, số nguyên tố gần nhất là',c[d])
        else: print(n,'không là số nguyên tố, số nguyên tố gần nhất là',c[d-1])
    return 
x=int(input('nhập số: '))
if x<2: print(x,'không là số nguyên tố, số nguyên tố gần nhất là 2')
else:
    a(x)
    
    
    

    