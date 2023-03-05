a=input("Nhập một chuỗi ký tự:")
dem=0
for i in a:
    if "0" <= i <="9":
        dem+=1
        print("Các số trong chuỗi ký tự vừa nhập là:")
        print(i,end=",")
print("Số các ký tự trong chuỗi là số = ",dem)  