# bài 3
x = float(input("nhập giá trị của x: "))
cos_x = 1 
a = 1 
b = 2
while abs(a) > 1e-4:
    a = -a*x**2/(b*(b-1)) 
    cos_x += a 
    b += 2 
print("giá trị xấp sỉ của cos", x, "là", cos_x)