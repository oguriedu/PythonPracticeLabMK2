x = float(input("Nhập giá trị của x: "))
cos_x = 1 
term = 1 
n = 2
while abs(term) > 1e-4:
    term = -term * x**2 / (n * (n - 1)) 
    cos_x += term 
    n += 2 
print("Giá trị gần đúng của cos", x, "là", cos_x)