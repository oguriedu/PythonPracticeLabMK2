str1= input(" nhập chuỗi ký tự str1:")
str2=input(" nhập chuỗi ký tự str2 :")
k=""
h= 0 
for i in str1:
    if h < len(str2):
        k+=i+str2[h]
    else:
        k += i
    h += 1
print (k) 

