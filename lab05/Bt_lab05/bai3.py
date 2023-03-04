n=int(input('Nhập giá trị'))
a=[]
while(n>0):
    x=n%2
    a.append(x)
    n=(n-x)/2
    a.reverse()
print(a)


