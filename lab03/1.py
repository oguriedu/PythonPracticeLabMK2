n=int(input('Nhap n: '))
sum,j = 1, 1
for i in range(0,n+1):
    j*=((2*i+2)/(2*i+3))
    sum+=j
print(round(sum,3))
