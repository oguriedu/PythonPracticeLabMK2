print('Nhập a1,b1,c1:')
a1=float(input('a1='))
b1=float(input('b1='))
c1=float(input('c1='))
print("Nhập a2,b2,c2:")
a2=float(input('a2='))
b2=float(input('b2='))
c2=float(input('c2='))
d=a1*b2-a2*b1
dx=c1*b2-c2*b1
dy=a1*c2-a2*c1
if d!=0:
    print('phuoqng trình có nghiêmj duy nhất x=%0.2f và y=%0.2f'%((dx/d),(dy/d)))
else:
    if dy==0 and dx==0:
        print("Vô định")
    else:
        print("Vô nghiệm")
print('Chương trình phân loại sinh viên.')
print('Nhập điểm sinh viên,',end='')
loai=input("điểm:")
if loai=='A' : print("Xếp loại xuất sắc.")
elif loai=='B' : print("Xếp loại Giỏi.")
elif loai=='C' : print("Xếp loại Khá.")
elif loai=='D' : print("Xếp loại Trung Bình.")
elif loai=='E' : print("Xếp loại Yếu.")
elif loai=='F' : print("Xếp loại Kém.")
else:
    print("Nhập sai xin mời nhập lại điểm!")
        
        
