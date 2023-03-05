str1=input('mời nhập chuỗi 1: ')
str2=input("mời nhập chuỗi 2: ")
chuoi_chung = ""
len1, len2 = len(str1), len(str2)
for i in range(len1):
    for j in range(len2):
        so = 0
        giong = ''
        while ((i+so < len1) and (j+so<len2) and str1[i+so] == str2[j+so]):
            giong += str2[j+so]
            so += 1
        if len(giong) > len(chuoi_chung):
            chuoi_chung = giong
    

print(chuoi_chung)
