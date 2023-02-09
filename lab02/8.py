TNCT=int(input('Nhập thâm niên công tác của nhân viên: '))
if TNCT<12:
    he_so=2.34
elif 12<=TNCT<36:
    he_so=3.33
elif 36<=TNCT<60:
    he_so=3.66
elif TNCT>=60:
    he_so=3.99
print('Lương của nhân viên là {:,} Đồng'.format(int(he_so)*1350000))