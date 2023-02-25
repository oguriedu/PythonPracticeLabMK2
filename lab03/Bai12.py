n=input('Nhập số container : ')
A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
B=[10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]
s1=0
s2=0
for i in range(0,4):
    a=B[A.index(n[i])]*(2**i)
    s1+=a
for i in range(4,10):
    b=int(n[i])*(2**i)
    s2+=b
s=s1+s2
kq=s%11
print('Số kiểm tra :',kq)