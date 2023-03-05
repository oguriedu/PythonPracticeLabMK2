#chương trình trộn hai chuỗi kí tự được nhập từ bàn phím
str1=input("nhập chuỗi kí tự thứ nhất = ")
str2=input("nhập chuỗi kí tự thứ hai = ")
print("chuỗi kí tự thứ nhất mà bạn nhập là : ",str1)
print("chuỗi kí tự thứ hai mà bạn vừa nhập là : ",str2)
#trộn hai chuỗi đan xen các phần tử
do_dai_str1=len(str1)
do_dai_str2=len(str2)
i=0
while i < do_dai_str1 or i < do_dai_str2:
    if i < do_dai_str1:
        print(str1[i],end="")
    if i < do_dai_str2:
        print(str2[i],end="")
    i=i+1