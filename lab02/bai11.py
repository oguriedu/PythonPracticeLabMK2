#
from datetime import datetime
a=input("Nhập ngày và tháng (cách nhau bởi dấu ;): ")
b=a.split(";")
while True:
    try:
        datetime(2023,int(b[1]),int(b[0]))
        break
    except ValueError:
        print("Ngày tháng không hợp lệ")
        a=input("Nhập ngày và tháng (cách nhau bởi dấu ;): ")
        b=a.split(";")
if b[0]=="31"and (b[1]=="1" or b[1]=="3" or b[1]=="5" or b[1]=="7" or b[1]=="8" or b[1]=="10" ):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,int(b[1])+1))
elif b[0]=="31"and (b[1]=="12" ):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,1)) 
elif b[0]=="30"and (b[1]=="4" or b[1]=="6" or b[1]=="9" or b[1]=="11" ):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,int(b[1])+1))
elif b[0]=="28"and (b[1]=="2"):
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,3))
else:
    print("Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],int(b[0])+1,(b[1])))