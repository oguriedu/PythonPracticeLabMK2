def tlct():
    a = int(input('Nhập thâm niên công tác:'))
    if a < 12:
        hs = 2.34
    elif a < 36:
        hs = 3.33
    elif a < 60:
        hs = 3.66
    else:
        hs = 3.99
    return hs
hs = tlct()
print('Lương=%0.3f đồng'%(1350000*hs))