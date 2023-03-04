str1 = input('nhập kí tự xâu thứ nhất: ')
str2 = input('nhập kí tự xâu thứ hai: ')
xau_tron = ' '
vtstr1 = 0
vtstr2 = 0

while (vtstr1 < len(str1)) or (vtstr2 < len(str2)):
    if vtstr1 < len(str1):
        xau_tron += str1[vtstr1]
        vtstr1 += 1

    if vtstr2 < len(str2):
        xau_tron += str2[vtstr2]
        vtstr2 += 1
print('chuỗi sau khi trộn:', xau_tron)
