a,b,c=map(float, input('Nhập các giá trị a,b,c:').split())
'ax2 + bx +c =0'
del_ta= b*b - 4*a*c ; import math
if del_ta > 0 :
    x1=(-b - math.sqrt(del_ta))/(2*a)
    x2=(-b + math.sqrt(del_ta))/(2*a)
    print('phương trình có 2 nghiệm phân biệt : x1=',x1,'và x2=',x2)
if del_ta ==0 :
    x=-b/(2*a)
    print('phương trình có 2 nghiệm trùng nhau x1=x2=',x)
else :
    print('phương trình vô ngiệm')