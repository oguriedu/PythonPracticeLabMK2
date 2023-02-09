#chương trình tính tiền điện:
so_KW=int(input("Nhập số KW điện = "))
if so_KW>=0:
    if so_KW<=100:
        print("tiền điện phải trả là ",so_KW*2000,"đồng")
    elif so_KW>=101 and so_KW<=200:
        print("tiền điện phải trả là ",so_KW*2500,"đồng")
    elif so_KW>=201 and so_KW<=300:
        print("tiền điện phải trả là ",so_KW*3000,"đồng")
    elif so_KW>300:
        print("tiền điện phải trả là ",so_KW*5000,"đồng")
else:
    print("bạn đã nhập số điện không hợp lệ, vui lòng nhập lại cho chính xác")