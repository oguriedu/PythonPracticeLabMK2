str1 = input('nhập chuỗi kí tự str1:')
str2 = input('nhập chuỗi ký tự')
for i in str1:
    if i  not in str2:
        str1 = str1.replace(i,' ')
a = str1.split()

print(a)
if a == []:
    print('2 chuỗi str1 và str2 không có chuỗi ký tự con chung!')
else:
    max = 0
    for i in range(len(a)):
        if (len(a[i])) > len(a[max]):
            max = i
    print(f'chuỗi kí tự con chung của 2 chuỗi Str1 và Str2 có độ dài cực đại là: {a[max]}')
