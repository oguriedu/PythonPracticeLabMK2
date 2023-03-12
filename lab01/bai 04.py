import abc
import math
x = float(input('Nhập x = '))
a = (-x+math.sqrt(x**2+4))/(x**4+1)**(1/7)
print("f(x) = %0.2f" % a)
