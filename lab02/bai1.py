n=int(input("Nhập số tháng: "))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("Tháng",n,"có 31 ngày trong ")
elif n==2:
    print("Tháng",n,"có 28 nếu năm không nhuận và có 29 ngày nếu đó là năm nhuận")
elif n==4 or n==6 or n==9 or n==11:
    print("Tháng",n,"có 30 ngày")
elif n>12:
    print("Lỗi xác định ngày tháng!")