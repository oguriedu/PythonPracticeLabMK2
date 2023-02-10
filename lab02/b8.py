a=int(input("Nhập thâm niên công tác : "))
b=1350000
if a<12:
    print("Tiền lương là : ", b*2.34, 'đồng')
elif 12<=a<36:
    print("Tiền lương là : ", b*3.33, 'đồng')
elif 36<=a<60:
    print("Tiền lương là : ", b*3.66, 'đồng')
else:
    print("Tiền lương là : ", b*3.99, 'đồng')