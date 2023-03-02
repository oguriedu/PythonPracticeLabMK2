a=int(input("nhập số nguyên từ bàn phím: "))
binary=format(a,"b")
l=len(binary)-1
m=[]
for i in binary:
    if int(i)==1:
        m.append(f"2^{l}")
    l-=1
print("+".join(m))
