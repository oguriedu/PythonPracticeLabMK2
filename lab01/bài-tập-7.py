import math
a = float (input('nhập số a: '))
b = float (input ('nhập số b: '))
c = float (input ('nhập số c: '))

def tim_dinh(a, b, c):
    x = -b/(2*a)
    y = a*math.pow(x, 2)+b*x+c
    return (round(x, 2), round(y, 2))

print ('tọa độ đỉnh cần tìm: ', tim_dinh(a, b, c))