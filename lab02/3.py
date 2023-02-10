ngay_trong_tuan=int(input("mời nhập thứ trong tuần(1 đến 7): "))
thu=["thứ2","thứ3","thứ4","thứ5","thứ6","thứ7","chủ nhật"]
if ngay_trong_tuan in range(1,8):
    for i in range(1,len(thu)+1):
        if ngay_trong_tuan==i:
            print(thu[ngay_trong_tuan-1])
if ngay_trong_tuan>7 or ngay_trong_tuan<1:
    while True:
        nhap_lai=int(input("mời bạn nhập lại"))
        if nhap_lai in range(1,len(thu)+1):
            print(thu[nhap_lai-1])
            break