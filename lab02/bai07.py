'''Viết chương trình in ra học lực của học sinh'''
while True:
    choice=float(input("Nhập điểm TB của học sinh:"))
    if 0.0<choice<3.0:
        print("Loại Kém")
    if 3.0<choice<5.0:
        print("Loại Yếu")
    if 5.0<choice<6.5:
        print("Loại Trung Bình")
    if 6.5<choice<8.0:
        print("Loại Khá")
    else:
        if 8.0<choice<10.0:
            print("Loại Giỏi")