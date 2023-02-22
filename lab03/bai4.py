from argparse import _AppendAction


def check(n):
    check = True
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return check

n = int(input('Nhập n:'))
a  = []
print('các số nguyên tố bé hơn hoặc bằng n là:',end = ' ')
for i in range(n+1):
    if check(i) == True:
        a.append(i)
print(a)