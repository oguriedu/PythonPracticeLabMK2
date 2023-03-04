str1=input('moi nhap chuoi thu 1: ')
str2=input('moi nhap chuoi thu 2: ')
lst1=str1.strip().split(" ")
lst2=str2.strip().split(" ")
chung=''

if len(lst1)==len(lst2):
    for i in range(0,len(lst1)-1):
        if lst1[i]==lst2[i]:
            chung+=lst1[i]
        else:
            chung=''
print(chung)
