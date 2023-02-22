r = float(input('nhập bán kính khối trụ:'))
h = float(input('nhập chiều cao khối trụ:'))
sxq = h*r
st = r*r*3.14
stp = sxq +2*st
v = 3.14*r*r*h
print('\ndiện tích xung quanh: %0.2f\ndiện tích toàn phần: %0.2f \nthể tích khối trụ:%0.2f'%(sxq,stp,v))