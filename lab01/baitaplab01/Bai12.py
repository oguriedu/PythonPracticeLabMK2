import math
a=float(input("Nhập vận tốc xe ô tô đang chạy: "))
# Khi xe dừng hẳn thì vận tốc bằng 0 --> v(t)=0
t=a**4/math.log(5,4)
print("Thời gian ô tô đi được cho đến lúc dừng là : %0.2f"%t,"giây")