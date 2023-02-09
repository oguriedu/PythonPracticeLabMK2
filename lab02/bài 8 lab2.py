TNCT = int(input('nhập số tháng công tác: '))
def tinh_luong(TNCT):
    if TNCT >= 60:
        luong = 1350000 * 3.99
    elif TNCT >= 36:
        luong = 1350000 * 3.66
    elif TNCT >= 12:
        luong = 1350000 * 3.33
    else:
        luong = 1350000 * 2.34
    return luong
print ('lương nv nhận đc: ', tinh_luong(TNCT))