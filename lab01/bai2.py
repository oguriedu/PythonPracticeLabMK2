d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))

# Tính tổng số giây
tong_so_giay = d*24*60*60+h*60*60+m*60+s

# Đổi từ giây sang ngày, giờ, phút, giây
days = tong_so_giay // (24 * 60 * 60)
hours = (tong_so_giay % (24 * 60 * 60)) // (60 * 60)
minutes = (tong_so_giay % (60 * 60)) // 60
seconds = tong_so_giay % 60

# In kết quả
print("Tổng số giây:", tong_so_giay)
print("Tổng số ngày, giờ, phút, giây:", days, "ngày,", hours, "giờ,", minutes, "phút,", seconds, "giây.")
