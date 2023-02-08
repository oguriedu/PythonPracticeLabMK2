
a=int(input('nhập a: '))
b=int(input('nhập b: '))
c=int(input('nhập c: '))
t=round(-b/(2*a),2)
print("đỉnh của phương trình là:({},{}) ".format(t,round(a*t*t+b*t+c,2)))
