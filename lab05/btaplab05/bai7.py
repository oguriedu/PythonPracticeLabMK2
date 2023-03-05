n=input('Nhập từ cần tìm:')
t=input('Nhập văn bản:')
for i in list(t.split()):
    if n == i:
        break
print('Số từ cần tìm có trong văn bản là:',((t.split()).count(n)))