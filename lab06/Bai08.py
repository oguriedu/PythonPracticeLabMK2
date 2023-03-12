n=int(input('Nhập n: '))
a = [0, 1]
while True:
    b=a[-1]+a[-2]
    a.append(b)
    if len(a)-1==n:
        break
print('Dãy Fibonacci: ',a)