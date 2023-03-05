str1 = input('nhập str1:')
str2 = input('nhập str2:')
a = 0
print('chuỗi str sau khi trộn:',end='')

if len(str1) > len(str2):
    for i in str1:
        print(i,end='')
        if a < len(str2):    
            print(str2[a],end='')
            a += 1
else:
    for i in str1:
        print(i,end='')
        print(str2[a],end='')
        a += 1
    for i in range(a,len(str2)):
        print(str2[i],end='')
