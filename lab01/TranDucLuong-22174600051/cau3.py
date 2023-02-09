import math 
from tabulate import tabulate
A=[['1','DientichXungquanh'],['2','DienTichToanPhan'],['3','TheTich']]
B=['x','y']
R=eval(input("Enter the radius(cm):"))
h=eval(input("Enter the height(cm):"))
Sxq=2*3.14*R*h
Stp=2*3.14*math.pow(R,2)
V=(2*3.14*R*h)+(2*3.14*math.pow(R,2))
print(tabulate(A,headers=B,tablefmt='fancy_grid'))
op=int(input("Enter the option:"))
if op==1:
    print('Dien tich xung quanh cua hinh tru là:',Sxq,'cm2')
elif op==2:
    print("Dien tich toan phan cua hinh tru la",Stp,'cm2')
else:
    print("The tich hinh tru la:",V,'cm3')