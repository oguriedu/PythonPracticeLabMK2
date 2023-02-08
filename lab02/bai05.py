thang=int(input("Nhập tháng : "))
while True:
    if thang<1 or thang>12:
        print("Bạn đã nhập sai , hãy nhập lại!")
        thang=int(input("Nhập tháng : "))
    else:
        break
if thang==1:
    print('Tháng 1:January')
elif thang==2:
    print('Tháng 2:February')
elif thang==3:
    print('Tháng 3:March')
elif thang==4:
    print('Tháng 4:April')
elif thang==5:
    print('Tháng 5:May')
elif thang==6:
    print('Tháng 6:June')
elif thang==7:
    print('Tháng 7:July')
elif thang==8:
    print('Tháng 8:August')
elif thang==9:
    print('Tháng 9:September')
elif thang==10:
    print('Tháng 10:October')
elif thang==11:
    print('Tháng 11:November')
elif thang==12:
    print('Tháng 12:December')