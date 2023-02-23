a=input("nhập tử số và mẫu số(cách nhau bởi dấu ;): ")
ka=a.split(";")
h=0
while ka[1]=="0":
    print("mẫu số lỗi mời nhập lại")
    h=input("nhập lại mẫu số: ")
    ka[1]=h
print(ka)