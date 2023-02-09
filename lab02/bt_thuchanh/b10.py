print("khung giờ từ 5h đến 22h")
k=input("nhập giờ bắt đầu và kết thúc(cách nhau bởi giấu ;) thuê sân: ")
b=k.split(";")
while (int(b[0])<5)or(int(b[1])>22):
    print("khung giờ không hợp lệ")
    k=input("nhập giờ bắt đầu và kết thúc(cách nhau bởi giấu ;) thuê sân: ")
a=int(b[1])-int(b[0])
if(a<=3):
     a= a*100000
elif(a<=11):
     a= (a-3)*75000+300000
elif(a<=15):
     a=((((a-3)*75000+300000)*90)/100)
else:
     a= (a-3)*75000+300000
print("số tiền phải trả",a)