import math
a = int(input('Nhập hệ số a: '))
b = int(input('Nhập hệ số b: '))
c = int(input('Nhập hệ số c: '))
def giaiptb2(a,b,c):
    delta = math.pow(b,2)-4*a*c
    if a==0:
        print('Đây là phương trình bậc nhất có nghiệm là ',-c/b)
        if b==0 and c==0:
            print('Phương trình có vô số nghiệm ')
        if b==0 and c!=0:
            print('Phương trình vô nghiệm ')
    else:
        if delta==0:
            x = -b/2*a
            print('Phương trình có nghiệm kép: ',x)
        elif delta>0:
            x1 = -b+math.sqrt(delta)/2*a
            x2 = -b-math.sqrt(delta)/2*a
            print('Phương trình có 2 nghiệm phân biệt x1 và x2 lần lượt là: ',x1,x2)
        else:
            x1 =  (-b+math.sqrt(abs(delta)))/(2*a)
            x2 =  (-b-math.sqrt(abs(delta)))/(2*a)
            print("Phương trình có 2 nghiệm phức :",x1,"*i","và",x2,"*i")
    return
giaiptb2(a,b,c)