n=int(input("moi nhap so tu nhien: "))
while True:
    if n<=0:
        n=int(input("so tu nhien phai lon hon khong, moi nhap lai: "))
    if n>0:
        break

bit=" "
while n//2!=0:
    nhi_phan=n%2
    bit+=str(nhi_phan)
    n=(n-nhi_phan)//2
    bit+=" "
    if n//2==0:
        nhi_phan=n%2
        bit+=str(nhi_phan)
print("".join(list(reversed(bit.split()))))
