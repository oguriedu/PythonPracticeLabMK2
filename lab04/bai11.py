import os
drink=["cafe","cam vắt","nước ép cà rốt","nước lọc","nước dừa"]
l=[]
n=1
while True:
    if n==1:
        os.system("cls")
        print("Menu:")
        print("1. Cafe")
        print("2. Cam vắt")
        print("3. Nước ép cà rốt")
        print("4. Nước lọc")
        print("5. Nước dừa")
        order = int(input("Chọn thức uống theo số trên menu: "))
        try:
            l.append(drink[order-1])
            n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4:xóa order cũ "))
        except:
            print("Số bạn chọn không hợp lệ. Vui lòng thử lại.")
            n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4:xóa order cũ "))
    elif n==3:
        break
    elif n==2:
        os.system("cls")
        for i in l:
            print(f"bạn đã chọn {i}")
        n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4: xóa order cũ "))
    elif n==4:
        os.system("cls")
        for i in l:
            print(f"bạn đã chọn {i}")
        deleteorder=int(input("nhập thứ tự order muốn xóa: "))
        try:
            l.pop(deleteorder-1)
            n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4: xóa order cũ "))
        except:
            print("thứ tự không hợp lệ")
            n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4: xóa order cũ "))
    else:
        print("lựa chọn của bạn không hợp lệ")
        n=int(input("bạn muốn làm gì tiếp: 1:chọn đồ tiếp ,2:xem lại order, 3:dừng lại, 4: xóa order cũ "))
os.system("cls")
if len(l)>=1:
    for i in l:
        print(f"bạn đã chọn {i}")
else:
    print("bạn không chọn gì")
    