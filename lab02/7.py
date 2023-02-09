a=float(input('Nhập điểm TK: '))
if 0<=a<4:
    print('Loại kém')
elif a<=4<5:
    print('Loại yếu')
elif a<=5<=6:
    print('Loại trung bình')
elif 6<a<=8:
    print('Loại khá')
elif 8<a<=10:
    print('Loại giỏi')
else:
    print('Vui lòng nhập điểm TK hợp lệ')