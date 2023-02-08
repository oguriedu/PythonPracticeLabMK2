import math
def the_tich(r,h):
      S = lambda r,h: math.pi*r*r*h
      return S(r,h)
def sxq(r,h):
      S = lambda r,h: math.pi*2*r*h
      return S(r,h)
def stp(r,h):
      S = lambda r,h: math.pi*2*r*r*h+math.pi*r*2*h
      return S(r,h)


r=float(input('Nhập bán kính :'))
h=float(input('Nhập chiều cao:'))

print("Diện tích xung quanh là :  %0.2f"%sxq(r,h))
print("Diện tích toàn phần là : %0.2f"%stp(r,h))
print("Thể tích là : %0.2f"%the_tich(r,h))
