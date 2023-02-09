a=0
vec1=[]
toa_do1=int(input("vecto này có bao nhiêu tọa độ?"))
while True:
    a+=1
    nhap=int(input("nhập tọa độ: "))
    vec1.append(nhap)
    if a==toa_do1:
        break
b=0
vec2=[]
toa_do2=int(input("vecto nay co bao nhieu toaj do?"))
if toa_do1!=toa_do2:
    print("phai co so toa do giong nhau moi co tich vo huong")
while True:
    b+=1
    nhap=int(input("nhap toa do: "))
    vec2.append(nhap)
    if b==toa_do2:
        break
vec=[]
for i in range (len(vec1)):
    for j in range (len(vec2)):
        tich=vec1[i]*vec2[j]
        if i==j:
            vec.append(tich)
                
print("tich vo huong cua 2 vecto la",sum(vec))
    