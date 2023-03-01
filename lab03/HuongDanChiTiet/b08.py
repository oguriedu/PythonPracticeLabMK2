a = int(input('Nhập số a = '))
b = int(input('Nhập số b = '))
if a == b == 0:
    print("Hai số 0 không có UCLN \n")
else:
    if a != 0 and b == 0:
        print('UCLN(', a, ',', b, ')=', abs(a))
    else:
        if a == 0 and b != 0:
            print('UCLN(', a, ',', b, ')=', abs(b))
        else:
            if a < b:
                min = a
            else:
                min = b
            for i in range(1, min+1):
                if a % i == 0 and b % i == 0:
                    ucln = i
            print('UCLN(', a, ',', b, ')=', ucln)
