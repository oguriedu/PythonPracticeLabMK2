x = float(input("Nhập giá trị của x: "))
cos_x = 1 
m = 1 
n = 2
while abs(m) > 1e-4:
    m = -m * x**2 / (n * (n - 1)) 
    cos_x += m 
    n += 2 
print("Giá trị xấp sỉ của cos", x, "là", cos_x)