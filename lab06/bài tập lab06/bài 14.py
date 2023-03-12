import re
Name = input('nhập tên người dùng: ')
Pass_list = [num for num in input('nhập mật khẩu:').split(',')]
Pass_right = []
for i in Pass_list:
    if len(i)<=6 and len(i)>=12:
        continue
    else:
        pass
    if re.search('[a-z]', i) == None:
        continue
    elif re.search('[A-Z]', i) == None:
        continue
    elif re.search('[0-9]', i) == None:
        continue
    elif re.search('[$#@]', i) == None:
        continue
    else:
        Pass_right.append(i)
print('mật khẩu hợp lệ: ', Pass_right)