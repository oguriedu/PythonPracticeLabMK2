'''
lồng 2 str
'''
a1 = input('nhập chuỗi thứ nhất: ')
a2 = input('nhập chuỗi thứ hai: ')
b1 = 0
b2 = 0
a = ""
while b1 < len(a1) or b2 < len(a2):
    if b1 < len(a1):
        a = a + a1[b1]
        b1 = b1 + 1
    if b2 < len(a2):
        a = a + a2[b2]
        b2 = b2 + 1
print("chuỗi sau khi lồng: ", a)
