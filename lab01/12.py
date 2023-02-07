import math
a = float(input('Nhập vào vận tốc ban đầu của xe ô tô (m/s): '))
t = 0
v = a
while v > 0:
    t += 0.01
    v = -t * math.log(4,5) + a**4
print("Thời gian ô tô dừng là:", round(t, 2) , "giây")