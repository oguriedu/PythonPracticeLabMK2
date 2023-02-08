u=220
i=2.7
"giá tiền là 7000đ/kwh"

t=eval(input("nhập số thời gian sử dụng(tính bằng giây)"))
A=(u*i)/1000*(t/3600)
m=A*7000
print("số tiền bạn cân phải trả cho ",t,"giây sử dụng là",round(m,2),"đồng")