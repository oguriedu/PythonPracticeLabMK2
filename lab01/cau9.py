from tabulate import tabulate
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
A=[a,b,c]
print("tọa độ điểm A trong không gian:",A)
I=['0','điểm đối xứng qua mặt phẳng']
Y=[['Oxy'],['Oxz'],['Oyz']]
print(tabulate(Y,headers=I,tablefmt='fancy_grid', showindex='always'))
ch=int(input('nhập lựa chọn: '))
if ch==0:
    print('tọa độ điểm đối xứng: ', [a,b,-c])
elif ch==1:
    print('tọa độ điểm đối xứng:  ', [a,-b,c])
elif ch==2:
    print('tọa độ điểm đối xứng: ', [-a,b,c])
else: 
    print ('nhập sai, mời nhập lại: ')