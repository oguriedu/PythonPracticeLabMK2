bang={'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,\
      'R':29,'S':30,'T':31,'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38}
c=(input("Nhập số của container (4 ký tự đầu là chữ cái,6 số sau là chữ số): "))
m=0
d=0
s=0
for i in c:
    if d<4:
        s+=(bang[i]*2**m)
    else:
        s+=(int(i)*2**m)
    d+=1
    m+=1
print(s%11)
