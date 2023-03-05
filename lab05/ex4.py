str1=input("nhập str1 : ")
str2=input("nhập str2 : ")
a=""
l=0
for i in str1:
    if l <len(str2):
        a+=i+str2[l]
    else:
        a+=i
    l+=1
print(a)