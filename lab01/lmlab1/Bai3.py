r=float(input("Nhập bán kính: "))
h=float(input("Nhập chiều cao: "))
a=2 * 3.14 * r * h
b= 2*3.14 * r * (r + h)
c=3.14*r*2*h
a = round(a, 2)
b = round(b, 2)
c= round(c,2)
print("Diện tích xung quanh là :",a)
print("Diện tích toàn phần là :",b)
print("thể tích hình trụ là :",c)