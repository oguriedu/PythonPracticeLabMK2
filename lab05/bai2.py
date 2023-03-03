str = input('Nhập str: ')
print('Chuỗi kí tự vừa nhập là: ',str)
dem1 = 0
dem2 = 0
for i in str:
    if '0' <=i<='9':
        dem1+=1
for i in str:
    if 'a'<=i<='z' or 'A' <=i<='Z':
        dem2+=1
print(f'số kí tự là chữ số là: {dem1}')
print(f'số kí tự là tiếng anh là: {dem2}')
Footer
