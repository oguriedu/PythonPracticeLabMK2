thang=int(input("Nhập tháng cần tìm: "))
if thang==1:
    print("tháng 1 có 31 ngày")
elif thang==2:
    print("Nhập năm để xác định tháng 2 có bao nhiêu ngày")
    nam=int(input("Nhập năm:"))
    if ((nam % 4 == 0) and (nam % 100 != 0)):
        print("tháng 2 có 29 ngày")
    else:
        print("tháng 2 có 28 ngày")
elif thang==3:
    print("tháng 3 có 31 ngày")
elif thang==4:
    print("tháng 4 có 30 ngày")
elif thang==5:
    print("tháng 5 có 31 ngày")
elif thang==6:
    print("tháng 6 có 30 ngày")
elif thang==7:
    print("tháng 7 có 31 ngày")
elif thang==8:
    print("tháng 8 có 30 ngày")
elif thang==9:
    print("tháng 9 có 31 ngày")
elif thang==10:
    print("tháng 10 có 30 ngày")
elif thang==11:
    print("tháng 11 có 31 ngày")
elif thang==12:
    print("tháng 12 có 30 ngày")