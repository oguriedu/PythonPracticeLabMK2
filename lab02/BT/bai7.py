n=float(input("nhập điểm trung bình : "))
if n<4:
    print("loại kém ")
elif n==4:
    print("loại yếu")
elif n>=5 and n<=6:
    print("loại trung bình ")
elif n>=7 and n<=8:
    print("loại khá")
else: 
    print("loại giỏi")