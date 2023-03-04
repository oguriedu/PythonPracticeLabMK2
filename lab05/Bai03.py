n=int(input('Nhập 1 số tự nhiên n: '))
m=[]
while True:
    a=n%2
    m.append(str(a))
    n//=2
    if n==0:
        break
m.reverse()
str=''.join(m)
print('Chuyển sang hệ nhị phân : {}'.format(str))
