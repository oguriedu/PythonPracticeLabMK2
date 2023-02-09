tnct=int(input("Nhập thâm niên công tác : "))
a=1350000
if tnct<12:
    print("Tiền lương là : ", a*2.34, 'đồng')
elif 12<=tnct<36:
    print("Tiền lương là : ", a*3.33, 'đồng')
elif 36<=tnct<60:
    print("Tiền lương là : ", a*3.66, 'đồng')
else:
    print("Tiền lương là : ", a*3.99, 'đồng')