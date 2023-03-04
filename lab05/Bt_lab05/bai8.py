Str=input('Nhập chuỗi ký tự:')
max_len = 0
cur_len = 0
start_index = 0
cur_ky_tu = ''
max_ky_tu = ''
for i in range(len(Str)):
    if Str[i] == cur_ky_tu:
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
            max_ky_tu = cur_ky_tu
        cur_len = 1
        cur_ky_tu = Str[i]
        start_index = i
if cur_len > max_len:
    max_len = cur_len
    max_ky_tu = cur_ky_tu

print(max_ky_tu * max_len)
