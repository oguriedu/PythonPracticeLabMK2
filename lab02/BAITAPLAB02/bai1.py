a=int(input("Nhập tháng: "))
if a==1 or a==3 or a==5 or a==7 or a==12:
    print("Tháng",a,"có 31 ngày")
elif a==4 or a==6 or a==9 or a==11:
    print("Tháng",a,"có 30 ngày")
else:
    print("Tháng 2 có 28 ngày hoặc 29 ngày")