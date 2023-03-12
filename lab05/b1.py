str=input("nhập chuỗi ký tự:")
print("chuỗi ký tự vừa nhập",str)
dem=0
for c in str:
    if "0" <= c <= "9":
        dem+=1
        print("số các ký tự là số trong chuỗi đã nhập=",dem)