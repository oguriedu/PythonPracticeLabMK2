n = int(input('nhập số tự nhiên n: '))
i=[]
while n>0:
    i.append(str(n%2))
    n//=2
i.reverse()
i=''.join(i)
    
print(i)

