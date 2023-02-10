#
nam = int(input('Nhập năm: '))
thang = int(input('Nhập tháng: '))
def ngay(thang,nam):
    if nam%4==0 or nam%400==0 and nam%100!=0:
        if thang==1 or thang==3 or thang==5 or thang ==7 or thang == 8 or thang==10 or thang==12:
            print('tháng',thang,'có 31 ngày')
        elif thang==2:
            print('tháng',thang,'có 29 ngày')
        else:
            print('tháng',thang,'có 30 ngày')
    else:
        if thang==1 or thang==3 or thang==5 or thang ==7 or thang == 8 or thang==10 or thang==12:
            print('tháng',thang,'có 31 ngày')
        elif thang==2:
            print('tháng',thang,'có 28 ngày')
        else:
            print('tháng',thang,'có 30 ngày')
    return
ngay(thang,nam)