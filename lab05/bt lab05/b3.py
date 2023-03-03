A = int(input('nhập số tự nhiên n : '))
i=[]
while A>0:
    i.append(str(A%2))
    A//=2
i.reverse()
i=''.join(i)
    
print(i)