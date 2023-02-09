x,y,z=map(float, input('Nhập các giá trị x, y,z của đỉnh A:').split())
x2,y2,z2=map(float, input('Nhập các giá trị x, y,z của đỉnh B:').split())
x3,y3,z3=map(float, input('Nhập các giá trị x, y,z của đỉnh C:').split())
list=[]
d1=(x+x2+x3)/3
d2=(y+y2+y3)/3
d3=(z+z2+z3)/3
print("trọng tâm tam giác là:%0.2f"%d1,d2,d3)