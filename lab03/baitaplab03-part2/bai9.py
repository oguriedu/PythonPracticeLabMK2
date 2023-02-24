s=0
n=int(input('Nhập giá trị n:'))
if n < 0:
    print('hãy nhập lại!')
else:
    #S4 = 1^2 + 2^2 + 3^2 + … + n^2
    for i in range(1,n+1):
        s+=i**2
print('tổng của dãy số là:',s)
#S5 = 1^3 + 3^3 + 5^3 + … +(2n+1)^3
for i in range(1,n+1,2):
    s+=(2*i+1)**3
print('tổng của dãy số là:',s)
#S6 = 2^4 + 4^4 + 6^4 + … +(2n)^4
for i in range(-2,n+1,2):
    s += (2*n)**4
print('tổng của dãy số là:',s)