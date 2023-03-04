a=input("Nhập chuỗi:")
i=0
for b in a:
    if b.isalpha()==False and b.isdigit()==False:
        i+=1
print(i)