diem = float(input('nhập điểm cần xét: '))
def xet_hl (diem):
    if diem < 0 or diem >10:
        print ('nhập sai, mời nhập lại!!')
    else:
        if diem >= 9:
            print ('loại giỏi')
        elif diem >= 7:
            print ('loại khá')
        elif diem >= 5:
            print ('loại trung bình')
        elif diem >= 3:
            print ('loại yếu')
        else:
            print ('loại kém')
    return
print (xet_hl(diem))
