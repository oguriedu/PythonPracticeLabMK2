'''Viết chương trình xuất ngày tiếp theo của 1 ngày cho trước '''
from datetime import datetime
a=int(input("Nhập ngày:"))
b=int(input("Nhập tháng:"))
while True:
    try:
        datetime(2023,b,a)
        break
    except ValueError:
        print("Nhập sai ngày tháng")
        a=int(input("Nhập ngày:"))
        b=int(input("Nhập tháng:"))
if a==31 and (b==1 or b==3 or b==5 or b==7 or b==8 or  b==9 or b==10):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(a,b,1,b+1))
if a==31 and b==12:
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(a,b,1,1))
if a==30 and (b==4 or b==6 or b==9 or b==11):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(a,b,1,b+1))
if a==28 and b==2:
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(a,b,1,3))
else:
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(a,b,a+1,b))

    
