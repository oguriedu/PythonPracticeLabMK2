#nhập chuỗi từ bàn phím
s=input('nhập chuỗi:')
print('chuỗi ký tự vừa nhập là:',s)
count=0
dem=0
for char in s:
    if 'a'<= char <='z'or 'A'<= char <= 'Z'or '0'<= char <='9':
        count+=1   
    else:
        dem+=1
print('số ký tự không là chữ tiếng anh hoặc số là:',dem)
