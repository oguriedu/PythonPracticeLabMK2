n = int(input('nhập n: '))
def fibon(i):
    if i == 0:
        return 0
    elif 0 < i <= 2:
        return 1
    else:
        return fibon(i-1)+ fibon(i -2)

a = [fibon(x) for x in range(n+1)]
print('dãy fibonacci là: ',end='')
for i in range(len(a)-1):
    print(a[i],end=',')
print(a[-1])

