def tinh(n):
    s = 1
    for i in range(n):
        s = s*(2*(i+1))/(2*i+3) 
    return s
n = int(input('nhap so nguyen n:'))
sum = 0
for i in range(n+1):
    s = tinh(i)
    sum += s
print('tong day =%0.3f'%(sum))