Str=input("Nhập chuỗi kí tự:")
print("In ra chuỗi kí tự vừa nhập:",Str)
dem=0
for c in Str:
    if "0"<=c<="9":
        dem+=1
print("Chuổi kí tự là số:",dem)