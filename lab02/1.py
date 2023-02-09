#1
thang=int(input("tháng:"))
nam=int(input("năm"))
if (thang==1) :
    print("số ngày",31)
elif(thang==2):
    if(nam%4==0):
        print("sô ngày:",28)
    else:
        print("số ngày:",29)
elif(thang==3):
    print("số ngày",31)
elif(thang==4):
    print("số ngày",30)
elif(thang==5):
    print("số ngày",31)
elif(thang==6):
    print("số ngày",30)
elif(thang==7):
    print("số ngày",31)
elif(thang==8):
    print("số ngày",31)
elif(thang==9):
    print("số ngày",30)
elif(thang==10):
    print("số ngày",31)
elif(thang==11):
    print("số ngày",30)
elif(thang==12):
    print("số ngày",31)
else:
    print("không tồn tại ")