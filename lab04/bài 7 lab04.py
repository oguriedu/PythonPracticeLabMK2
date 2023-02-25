a = int (input('nhập số a: '))
b = int (input('nhập số b: '))
c = a*b
if a<b:
    t=a; a=b; b=t
while a!=b:
    p=a-b
    if p>b: a=p
    else: 
        a=b
        b=p
print('BCNN =', c/a)
    