thang=int(input("Nhập tháng : "))
while True:
    if thang<1 or thang>12:
        print("Nhập từ 1->12")
        thang=int(input("Nhập tháng : "))
    else:
        break
if thang==1:
    print('Tháng này là tháng 1')
elif thang==2:
    print('Tháng này là tháng 2')
elif thang==3:
    print('Tháng này là tháng 3')
elif thang==4:
    print('Tháng này là tháng 4')
elif thang==5:
    print('Tháng này là tháng 5')
elif thang==6:
    print('Tháng này là tháng 6')
elif thang==7:
    print('Tháng này là tháng 7')
elif thang==8:
    print('Tháng này là tháng 8')
elif thang==9:
    print('Tháng này là tháng 9')
elif thang==10:
    print('Tháng này là tháng 10')
elif thang==11:
    print('Tháng này là tháng 11')
elif thang==12:
    print('Tháng này là tháng 12')