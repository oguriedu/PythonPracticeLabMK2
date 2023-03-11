thang = int(input('Nhập số tháng bạn đã làm'))
luongcb = 1350000
if thang <12:
    luong = luongcb*2.34
elif (12<= thang < 36):
    luong = luongcb*3.33
elif (36<=thang<60):
    luong = luongcb*3.66
elif thang>=60:
    luong = luongcb*3.99
print('Lương của bạn là',luong)