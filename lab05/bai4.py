str1=input('Nhập str1 :')
str2=input('Nhập str2 :')

k=""
l=0
for i in str1:
    if l <len(str2):
        k+=i+str2[l]
    else:
        k+=i
    l+=1
print(k)