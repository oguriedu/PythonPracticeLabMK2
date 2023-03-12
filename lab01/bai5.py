import numpy as np
e=float(input("nhập toạ đọ thứ nhất của vecto a: "))
f=float(input("nhập toạ đọ thứ hai của vecto a: "))
g=float(input("nhập toạ đọ thứ nhất của vecto b: "))
h=float(input("nhập toạ đọ thứ hai của vecto b: "))
a = np.array([e,f]) 
b = np.array([g,h])
tich_vo_huong= np.dot(a,b)
print( " Tích vô hướng của 2 véc tơ là : ", tich_vo_huong)
