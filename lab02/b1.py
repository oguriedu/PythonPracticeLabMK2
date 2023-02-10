thang=int(input("Nhập tháng: "))
if(thang == 1 or thang ==  3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    print("Tháng này có 31 ngày")
elif(thang == 4 or thang == 6 or thang == 9):
    print("Tháng này có 30 ngày")
elif(thang == 2):
    print("Tháng này có 28 hoặc 29 ngày")
