n=int(input("nhap: "))
while True:
    if n<=0:
        n=int(input("so tu nhien phai lon hon 0, nhap lai ngay : "))
    if n>0:
        break
bit=""
while n//2!=0:
    nhi_phan=n%2
    bit+=str(nhi_phan)
    n=(n-nhi_phan)//2
    if n//2==0:
        nhi_phan=n%2
        bit+=str(nhi_phan)
print("chuoi nhi phan: ",bit.reverse())