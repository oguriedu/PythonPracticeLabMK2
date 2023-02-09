import math
while True:
    a=eval(input('a='))
    b=eval(input('b='))
    c=eval(input('c='))
    delta=pow(b,2)-4*a*c
    if delta<0:
        print("pt vô nghiệm")
    elif delta==0:
        print('x1=x2=',-b/(2*a))
    else:
        print('x1=',(-b+math.sqrt(delta))/(2*a))
        print("x2=",(-b-math.sqrt(delta))/(2*a))