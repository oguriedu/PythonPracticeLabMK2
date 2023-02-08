#chương trình đổi đơn vị thời gian
d=int(input("nhập số ngày = "))
h=int(input("nhập số giờ = "))
m=int(input('nhập số phút = '))
s=int(input("nhập số giây = "))
tong_so_giay=(d*24*3600)+(h*3600)+(m*60)+s
print('tổng số giây = ')
#thực hiện đổi 
ngay=tong_so_giay//(24*3600)
gio=(tong_so_giay%(24*3600))//(60*60)
phut=(tong_so_giay%(60*60))//60
giay=tong_so_giay%60
print("Tổng số giây:", tong_so_giay)
print("Tổng số ngày, giờ, phút, giây:", ngay, "ngày,", gio, "giờ,", phut, "phút,", giay, "giây.")