diem_tk=float(input('nhập điểm:'))
if diem_tk >=0 and diem_tk <=10:
    if diem_tk <3:
        print('học lực loại kém')
    elif diem_tk >=3 and diem_tk <5 :
        print('học lực loại yếu')
    elif diem_tk >=5 and diem_tk <6 :
        print('học lực loại trung bình')
    elif diem_tk >=7 and diem_tk <=8 :
        print('học lực loại khá')
    else :
        print('học lực loại giỏi ')
else :
    print('định dạng đầu vào không hợp lệ')
          