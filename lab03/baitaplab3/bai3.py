import math
n = int(input('nhập 1 số n:'))
h=n
m=n

if n< 2:
    print(f'{n} không là số nguyên tố')
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            print(f'{n}  không là số nguyên tố ')
            break
    else:
        print(f' là số nguyên tố ')    
while True:
    h-=1
    m+=1
    for i in range(2,h+1):
        if(h==i):
            print(h,"là số nguyên tố gần",n,'nhất')
            h='x'
            break
        if (h%i==0):
            break
    if ((h=='x')or (m=='x')):
        break
    break

