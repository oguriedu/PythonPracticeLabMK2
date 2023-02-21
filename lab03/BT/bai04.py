x = int(input('Nhập x: '))
def check_snt(x):
    flag = True
    if x<2:
        flag = False
    else:
        for i in range (2,x):
            if x%i==0:
                flag = False
    return flag
for i in range (1,x):
    if check_snt(i):
        print(i,end=' ')