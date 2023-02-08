a=float(input("nhập vào giá trị a: "))
b=float(input("nhập vào giá trị b: "))
c=float(input("nhập vào giá trị c: "))
x=-b/2*a
y=a*x**2+b*x+c

print("pt của bạn nhập vào là: ",str(a)+"(X)"+"^2"+"+"+str(b)+"X"+"+"+str(c))
print("đỉnh của phương trình là: ",round(x,2),round(y,2))