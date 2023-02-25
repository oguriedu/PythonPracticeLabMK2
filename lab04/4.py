tu_so= int(input("nhập tử số:"))
mau_so= int(input("nhập mẫu số:"))
phan_so= tu_so/mau_so 
while True:
    if mau_so==0:
        print("bạn phải nhập lại mẫu số:")
    if mau_so!=0:
        print("kết quả phân số là:", phan_so)
        break    