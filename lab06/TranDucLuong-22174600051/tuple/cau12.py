sumW = 0
sumD=0
while True:
    D=eval(input('Tien gui:'))
    if D=='end':
        break
    W=eval(input('Tien rut:'))
    sumD+=int(D)
    sumW+=int(W)
Total=sumD-sumW
if Total<0:
    print('So tien gui khong hop le!')
else:
    print(Total)