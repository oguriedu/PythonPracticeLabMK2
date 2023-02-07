a=input("nhap ma sv: ")
b=input("nhap ho ten: ")
c=input("nhap que quan: ")
d=input("nhap nam sinh: ")
i=int(input("nhap so nam hoc: "))
m=[]
for t in range(i):
    k=(input("nhap diem trung binh nam thu {}:".format(t+1)))
    m.append(k)
print("{:>15}{:>20}{:>15}{:>15}".format("ma sv","ho ten","que quan","nam sinh"))
print("{:>15}{:>20}{:>15}{:>15}".format(a,b,c,d))
for x in range(len(m)):
    print("diem trung nam thu",x+1,"la",m[x])

