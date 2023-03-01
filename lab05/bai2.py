a = input("nhập chuỗi bạn muốn")
a = a.lower()
a1 = 0
for i in a:
    if chr(ord('a')) <= i <= chr(ord('z')):
        a1 = a1 + 1
    if '0'<= i <= '9':
        a1 = a1 + 1
print('tổng số giá trị không phải chữ cái hoặc số có: ',len(a) - a1)
