import math
bk=float(input('nhập bán kính:'))
h=float(input('nhập chiều cao:'))
sxungquanh=2*math.pi*bk*h
sxungquanh=round(sxungquanh,2)
stoanphan=(2*math.pi*bk**2)+(2*math.pi*bk*h)
stoanphan=round(stoanphan,2)
skhoitru=math.pi*bk**2*h
skhoitru=round(skhoitru,2)
print('diện tích xung quanh khối trụ là:',sxungquanh)
print('diện tích toàn phần khối trụ là:',stoanphan)
print('thế tích khối trụ là:',skhoitru)