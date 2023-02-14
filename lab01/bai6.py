p=220*2.7 # là công suất
s=float(input("nhập thời gian sử dụng bóng đèn (giây) : "))
tien_dien= ((p*(s/3600))/1000)*7
print("số tiền điện phải thanh toán là: %0.3f"%tien_dien," nghìn đồng")
