a = input('nhập chuỗi nhị phân:')

def check(a):
    flag = True
    for i in a:
        if i == '1' or i == '0':
            continue
        else:
            flag = False
            break
    return flag
if check(a) == True:
    decimal = 0
    temp = 0
    for i in a:
        decimal += int(i)*2**temp
        temp +=1
    print('số nhị phân bày chuyển thành số thập phân là:',decimal)
else:
    print('đây không phải là chuỗi nhị phân!')
