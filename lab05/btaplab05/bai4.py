str1=input("Nhập chuỗi ký tự thứ nhất: ")
str2=input("Nhập chuỗi ký tự thứ hai: ")
k=""
l=0
for i in str1:
    if l <len(str2):
        k+=i+str2[l]
    else:
        k+=i
    l+=1
print(k)