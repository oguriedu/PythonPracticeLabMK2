#đếm các kí tự trong chuỗi nhập từ bàn phím
chuoi_ki_tu=input("nhập chuỗi kí tự mà bạn muốn đếm = ")
print("chuỗi kí tự bạn vừa nhập là: ",chuoi_ki_tu)
count=0
for c in chuoi_ki_tu:
    if "0" <=c<="9":
        count+=1
print("số các kí tự là số trong chuỗi kí tự vừa nhập là : ",count)