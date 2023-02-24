s=0
n=int(input('Nhập n:'))
if n < 0:
    print('hãy nhập lại!')
else:
    #tổng dãy số 1+2+3+..
    for i in range(1,n+1):
        s+=i
print('tổng của dãy số là:',s)
#tổng dãy số 1+3+5+...
for i in range(1,n+1,2):
    s+=2*i+1
print('tổng của dãy số là:',s)
#tổng dãy số 2+4+6+...
for i in range(2,n,2):
    s+= 2*n
print('tổng của dãy số là:',s)