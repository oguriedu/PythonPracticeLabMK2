n=input('Nhập 1 số: ')
i=0
s=0
while i<=(len(n)-1):
    s+=int(n[i])
    i+=1
print('Tổng các chữ số trong số {} là {}'.format(n,s))