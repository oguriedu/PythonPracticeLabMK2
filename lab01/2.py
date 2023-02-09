s=int(input("nhập giây: "))
m=int(input("nhập phút: "))
h=int(input("nhập giờ: "))
d=int(input("nhập ngày:"))
ngay_gio=d*24
gio_phut=h*60
phut_giay=m*60
ngay_phut=ngay_gio*60
ngay_giay=ngay_phut*60
gio_giay=gio_phut*60
giay_phut=s/60
giay_gio=giay_phut/60
giay_ngay=giay_gio/24
phut_gio=m/60
phut_ngay=phut_gio/24
gio_ngay=h/24

print("-----------------")
print("1: Đổi ngày sang giờ")
print("2: Đổi ngày sang phút")
print("3: Đổi ngày sang giây")
print("4: Đổi giờ sang giây")
print("5: Đổi giờ sang phút")
print("6: Đổi phút sang giây")
print("7: Đổi giờ sang ngày")
print("8: Đổi giây sang ngày")
print("9: Đổi giây sang giờ")
print("10: Đổi giây sang phút")

print("-----------------")

while True:
    muon=input("bạn muốn làm gì?: ")
    if muon==1:
        print(ngay_gio)
    elif muon==2:
        print(ngay_phut)
    elif muon==3:
        print(ngay_giay)
    elif muon==4:
        print(gio_giay)
    elif muon==5:
        print(gio_phut)
    elif muon==6:
        print(phut_giay)
    elif muon==7:
        print(gio_ngay)
    elif muon==8:
        print(giay_ngay)
    elif muon==9:
        print(giay_gio)
    else:
        print(giay_phut)
    break