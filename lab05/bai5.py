str = input('nhập chuỗi str:')
a = ''
for i in str:
    if i.isnumeric():
        a += i
    else:
        str = str.strip(i)
print(str)
print('chuỗi số là:',a)
try:
    a1 = int(a)
    check = True
    for i in range(2,a1):
        if a1 % i == 0:
            check = False
            break
    if check == False:
        print('chuỗi số không là số hoàn hảo!!')
    else:
        print('chuỗi số là số hoàn hảo')
except:
    print('chuỗi số không là số hoàn hảo!!!')