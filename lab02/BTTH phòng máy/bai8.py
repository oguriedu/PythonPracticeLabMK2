tnct=int(input("Nhập TNCT:"))
a=1350000
if tnct<12:
    print("Tiền lương là:",int(a*2.34))
elif 12<=tnct<36:
    print("Tiền lương là:",int(a*3.33))
elif 36<=tnct<60:
    print("Tiền lương là:", int(a*3.66))
else:
    print("Tiền lương là:", int(a*3.99))