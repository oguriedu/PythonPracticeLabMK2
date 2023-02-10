diem=int(input('nhập điểm: '))
while diem<0 or diem>10:
    diem=int(input("mời bạn nhập lại: "))
if diem>=0 and diem<=10:
    if diem >=0 and diem <3:
            print("Loại Kém")
    elif diem<=4:
            print("loại yếu")
    elif diem>=5 and diem <=6:
            print("loại trung bình")
    elif diem>=7 and diem<=8:
            print("loại Khá")
    else :
            print("loại giỏi")