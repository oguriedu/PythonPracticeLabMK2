num=int(input("moi nhap so nguyen : "))
total=1
a=1
for i in range(0,num):
    a*=(2*(i+1))/(2*i+3)
    total+=a
    i+=1
print("ket qua la:",round(total,3))
