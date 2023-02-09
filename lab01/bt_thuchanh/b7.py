import math
a,b,c=map(float, input('Nhập các giá trị a,b,c:').split())
x=(-b/2)*a
y=a*(x**2)+ b*x +c
print('đỉnh của pt bậc 2 có x là:%0.2f'%x)
print('đỉnh của pt bậc 2 có y là:%0.2f'%y)