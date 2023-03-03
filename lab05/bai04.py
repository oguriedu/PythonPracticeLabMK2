str1 = input('Nhập str1: ').split(',')
str2 = input('Nhập str2: ').split(',')
str1.extend(str2)     #ghép 2 str
print(str1)