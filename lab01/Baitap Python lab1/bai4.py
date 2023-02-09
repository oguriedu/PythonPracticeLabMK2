import math
x=int(input(" nhập x: "))
gia_tri=(-x+ math.sqrt(math.pow(x,2)+4))/math.pow(math.pow(x,4)+1,1/7)
print(round(gia_tri,2))