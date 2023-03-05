str=input("Hãy nhập một chuỗi ký tự: ")
print("Chuỗi ký tự vừa nhập là:",str)
count=0
for i in str:
    if i.isnumeric():
        count+=1
print("Số các ký tự là số trong chuỗi vừa nhập là:",count)