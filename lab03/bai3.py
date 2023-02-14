def check(n):
    check = True
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return check


n = int(input('Nhập số n:'))
a = [2]
if check(n) == True:
    print(n,'là số nguyên tố')
else:
    print(n,'không là số nguyên tố')
    for i in range(1,n):
        if check(i) == True:
            a.append(i)        
    print('số nguyên tố gần n nhất là:',a[-1])





        
