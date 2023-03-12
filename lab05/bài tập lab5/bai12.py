str1=input('Nhập chuỗi 1 (chỉ chứa kí tự số): ')
str2=input('Nhập chuỗi 2 (chỉ chứa kí tự số): ')
a=len(str1)//2
b=len(str2)//2
if len(str1)%2==0 and (len(str2)%2==0)and (int(str1[0:b])+int(str1[-a:])==int(str2[0:b])+int(str2[-b:])):
    print(str1[0:b],'+',str1[-a:],'=',str2[0:b],'+',str2[-b:])
elif len(str1)%2!=0 and (len(str2)%2!=0)and (int(str1[0:b+1])+int(str1[-a:])==int(str2[0:b+1])+int(str2[-b:])):
    print(str1[0:b+1],'+',str1[-a:],'=',str2[0:b+1],'+',str2[-b:])
elif len(str1)%2!=0 and (len(str2)%2==0)and (int(str1[0:b])+int(str1[-a:])==int(str2[0:b])+int(str2[-b:])):
    print(str1[0:b],'+',str1[-a:],'=',str2[0:b],'+',str2[-b:])
elif len(str1)%2==0 and (len(str2)%2!=0)and (int(str1[0:b+1])+int(str1[-a:])==int(str2[0:b+1])+int(str2[-b:])):
    print(str1[0:b+1],'+',str1[-a:],'=',str2[0:b+1],'+',str2[-b:])
else:
    print('Không tồn tại cách đặt ')

