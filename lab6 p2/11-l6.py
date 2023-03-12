import random
a=[]
n=int(input("so phan tu se nhap la:"))
for i in range(n):
    a.append(int(input(f"moi nhap phan tu thu {i+1}: ")))
print(a)
b=[j for j in a if j%3==0 and j %5!=0]
print(f"cac phan tu chia het cho 3 nhung khong chia het cho 5 {b}")
c=[k**2 for k in a ]
print(f"binh phuong cua list a {c}")
d=[random.choice(a) for i in range(len(a)-1) if random.choice(a)%3==0]
print(d)


