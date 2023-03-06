str = input("Nhập một chuỗi kí tự:  ")
print("Chuỗi kí tự vừa nhập là: ", str)
dem = 0 
for c in str: 
    if "0" <= c <= "9":
        dem+=1
print("Số các ký tự là số trong chuỗi đã nhập bằng ", dem)