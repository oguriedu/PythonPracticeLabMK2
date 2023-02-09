#chương trình in ra học lực của học sinh theo thang điểm cho trước:
diemTK=float(input("Nhập điểm tổng kết của học sinh : "))
if diemTK>=0.0 and diemTK<=10.0:
    if diemTK<=3.0:
        print("bạn có học lực kém")
    elif diemTK==4.0:
        print("bạn có học lực yếu ")
    elif diemTK>=5.0 and diemTK<=6.0:
        print("bạn có học lực trung bình ")
    elif diemTK>=7.0 and diemTK<=8.0:
        print("bạn có học lực khá")
    elif diemTK>=9.0 and diemTK<=10:
        print("bạn có học lực giỏi")
else:
    print("bạn đã nhập điểm số không phù hợp, vui lòng nhập lại cho đúng")