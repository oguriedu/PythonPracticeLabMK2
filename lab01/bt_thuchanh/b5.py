a,b,c=map(float, input('Nhập các giá trị a,b,c:').split())
e,g,f=map(float, input('Nhập các giá trị e,g,f:').split())
import numpy as np
A = np.array([a, b, c])
B = np.array([e, g, f])
#vector A = (a, b, c) vector B =(e, g, f), TVH = a*e +b*g +c*f
TVH =a*e +b*g +c*f
print("Tich vo huong", TVH)