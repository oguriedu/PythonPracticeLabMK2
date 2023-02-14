import math
v=int(input("Nhập vào vận tốc khi xe oto  đang chạy (đơn vị đo vận tốc): \n"))
t=1
vt=0
while t<=100:
    t+=1
    a=v/t
    vt=-t*math.log(5,4)+math.pow(a,4)
    if vt<=0:
        print("thời gian ô tô đi được từ lúc phanh đến lúc dừng lại là: ",t,"(đơn vị đo thời gian)")
        break