#chương tình tính tiền lương
tham_nien_cong_tac=int(input("Nhập thông tin về thâm niên công tác theo tháng của bạn "))
if tham_nien_cong_tac>0:
    if tham_nien_cong_tac<12:
        print("Lương của bạn theo thâm niên là : ",2.34*1350000,"đồng")
    elif tham_nien_cong_tac>=12 and tham_nien_cong_tac<36:
        print("lương của bạn theo thâm niên là : ",3.33*1350000,"đồng")
    elif tham_nien_cong_tac>=36 and tham_nien_cong_tac<60:
        print("lương của bạn theo thâm niên là : ",3.66*1350000,"đồng")
    elif tham_nien_cong_tac>=60:
        print("lương của bạn theo thâm niên là : ",3.99*1350000,"đồng")
else:
    print("bạn đã nhập sai thâm niên công tác,vui lòng nhập lại cho đúng")