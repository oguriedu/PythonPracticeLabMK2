def a(r,h):
    sxq=2*3.14*r*h
    return sxq
def b(r,h):
    stp=2*3.14*r*h+2*3.14*r**2
    return stp
def c(r,h):
    v=3.14*h*r**2
    return v

r=eval(input("nhập bán kính : "))
h=eval(input("Nhập chiều cao : "))
print("Diện tích xung quanh của hình trụ là :",round(a(r,h),2))
print("diện tích toàn phần của hình trụ là : ",round(b(r,h),2))
print("thể tích của hình trụ là: ",round(c(r,h),2))