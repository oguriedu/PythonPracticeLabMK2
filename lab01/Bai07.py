# Tìm đỉnh của phương trình bậc 2 ax^2+bx+c
a=float(input('Nhập a = '))
b=float(input('Nhập b = '))
c=float(input('Nhập c = '))
#Sử dụng công thức đỉnh để tìm giá trị x của đỉnh parabol.
#Đỉnh còn là trục đối xứng của phương trình. Công thức tìm
#giá trị x của đỉnh của một phương trình bậc hai là x = -b/2a. 
#Thay các giá trị tương ứng để tìm x:
x=-b/2*a
#Thay giá trị x vào phương trình ban đầu để tìm y. Khi bạn đã biết giá trị x,
#chỉ cần thay nó vào trong công thức ban đầu bạn sẽ được y.
#Bạn có thể coi công thức tính đỉnh của hàm bậc hai là (x, y) = [(-b/2a), f(-b/2a)].
y=a*x**2+b*x+c
print("Đỉnh của phương trình là : (",x,",",y,")")
