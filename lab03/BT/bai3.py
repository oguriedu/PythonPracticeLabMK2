x = int(input('Nhập x: '))
a = []
def check_snt(x):
    flag = True
    if x<2:
        flag = False
    else:
        for i in range (2,x):
            if x%i==0:
                flag = False
                
    return flag
if check_snt(x) is True:
    print('đây là số nguyên tố')
else:
    print('đây không phải số nguyên tố ')
    for i in range (1,x):
        if check_snt(i):
            a.append(int(i))
            
print(f'số nguyên tố gần {x} nhất là: ',(a[-1:]))