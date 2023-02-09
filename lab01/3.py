import math

#Nhập bán kính và chiều cao từ bàn phím
bk = float(input("Nhập bán kính: ")) 
chieuCao = float(input("Nhập chiều cao: "))

#Tính diện tích xung quanh
dtXungQuanh = 2 * math.pi * bk * chieuCao

#Làm tròn đến số thập phân thứ hai
dtXungQuanh = round(dtXungQuanh,2)

#Tính diện tích toàn phần
dtToanPhan = (2 * math.pi * bk**2) + (2 * math.pi * bk * chieuCao)

#Làm tròn đến số thập phân thứ hai
dtToanPhan = round(dtToanPhan,2)

#Tính thể tích khối trụ
theTichKhoiTru = math.pi * bk ** 2 * chieuCao

#Làm tròn đến số thập phân thứ hai
theTichKhoiTru = round(theTichKhoiTru,2)

#In kết quả
print("Diện tích xung quanh của khối trụ là:", dtXungQuanh) 
print("Diện tích toàn phần của khối trụ là:", dtToanPhan) 
print("Thể tích của khối trụ là:", theTichKhoiTru)