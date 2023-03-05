Str = input('nhập chuỗi:')
max = 0
for i in Str:
    count = Str.count(i)
    if count > max:
        max = count
for i in Str:
    if Str.count(i) == max:
        print(end = i)
 