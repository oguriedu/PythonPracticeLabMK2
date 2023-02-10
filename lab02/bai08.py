'''Viết chương trình tính lương của nhân viên theo TNCT'''
while True:
    choice=int(input("Nhập thâm niên công tác(tháng):"))
    luong_canban=1350000
    print("Lương căn bản là:",luong_canban)
    if choice<12:
        he_so=2.34
        print("TNCT là",choice,"tháng, hệ số =",he_so)
    if 12<=choice<36:
        he_so=3.33
        print("TNCT là",choice,"tháng, hệ số =",he_so)
    if 36<=choice<60:
        he_so=3.66
        print("TNCT là",choice,"tháng, hệ số =",he_so)
    if choice>=60:
        he_so=3.99
        print("TNCT là",choice,"tháng, hệ số =",he_so)
    tinh_luong=he_so*luong_canban
    print("Lương của nhân viên dựa theo thâm niên công tác là:",tinh_luong)