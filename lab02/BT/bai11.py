from datetime import datetime
k=input("nhập ngày và tháng(cách nhau bởi giấu ;): ")
b=k.split(";")
while True:
    try:
        datetime(2023,int(b[1]),int(b[0]))
        break
    except ValueError:
        print("ngày tháng không hợp lệ")
        k=input("nhập ngày và tháng(cách nhau bởi giấu ;): ")
        b=k.split(";")
if b[0]=="31"and (b[1]=="1" or b[1]=="3" or b[1]=="5" or b[1]=="7" or b[1]=="8" or b[1]=="10" ):
    print("ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,int(b[1])+1))
elif b[0]=="31"and (b[1]=="12" ):
    print("ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,1)) 
elif b[0]=="30"and (b[1]=="4" or b[1]=="6" or b[1]=="9" or b[1]=="11" ):
    print("ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,int(b[1])+1))
elif b[0]=="28"and (b[1]=="2"):
    print("ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],1,3))
else:
    print("ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}".format(b[0],b[1],int(b[0])+1,(b[1])))