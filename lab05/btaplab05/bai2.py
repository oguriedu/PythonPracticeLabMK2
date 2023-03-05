str=input("Hãy nhập chuỗi ký tự: ")
print("Chuỗi ký tự đó là:",str)
count=0
dem=0
for i in str:
    if i.isalpha():
        count+=1
    if i.isnumeric():
        dem+=1
print("Số ký tự không phải là số:",count)
print("Số ký tự không phải là chữ cái tiếng anh:",dem)
      