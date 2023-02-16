n = int(input('Nhập n: '))
is_prime = True
c,d=0,0
if n < 2:
    print('Số nguyên tố gần với 1 nhất là 2')
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, 'là số nguyên tố')
    else:
        for i in range(n + 1, 99999999):
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                c=i
                break
        for i in range(n - 1, 1,-1):
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                d=i
                break
        if (c-n)<(n-d):
            print(c,'là số nguyên tố gần với',n)
        else:
            print(d,'là số nguyên tố gần với',n)
            
