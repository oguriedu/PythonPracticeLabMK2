#12
import math
a = float(input('Nhập vào vận tốc ban đầu của xe ô tô (m/s): '))
t = a**4/math.log(4,5)
print("Thời gian ô tô dừng là:", round(t, 2) , "giây")
