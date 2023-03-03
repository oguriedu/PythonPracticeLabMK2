s=input("nhập chuỗi ký tự từ bàn phím: ")
t=0
for i in s:
    if i.isnumeric() or i.isalpha():
        t+=1
        
print("số kí tự không là tiếng anh và chữ số =",len(s)-t)