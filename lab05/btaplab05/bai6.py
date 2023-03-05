n = input('Nhập hệ Hex:')
if "0"<=n<= "9" and "A"<=n<="F":
    a=int("n",16)
    print('Đổi chuỗi từ hệ Hex sang hệ 10 :',a)
else:
    print('Hãy nhập đúng hệ Hex!!!')