nhap=int(input("nhập vào 1 tháng: "))
nam=int(input("nhập năm: "))
import calendar
if nhap==2:
    if calendar.isleap(nam)==True:
        print("tháng ",nhap,"có 29 ngày")
    else:
        print("tháng",nhap,"có 28 ngày")

thang_31=[1,3,5,7,8,10,12]
for i in range(len(thang_31)):
    if thang_31[i]==nhap:
        print("tháng",nhap,"có 31 ngày ")
thang_30=[4,6,9,11]
for p in range(len(thang_30)):
    if thang_30[p]==nhap:
        print('tháng',nhap,"có 30 ngày")  
        