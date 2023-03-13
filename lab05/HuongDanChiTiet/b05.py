S1 = input('Nhập chuỗi S1: ')
S2 = input('Nhập chuỗi S2: ')

i, j = 0, 0
while i < len(S1) and j < len(S2):
    if S1[i] == S2[j]:
        j += 1
    i += 1

if j == len(S2):
    print("Yes, có thể nhận được S2 từ S1 bằng cách xóa đi một số ký tự.")
else:
    print("No, không thể nhận được S2 từ S1 bằng cách xóa đi một số ký tự..")
