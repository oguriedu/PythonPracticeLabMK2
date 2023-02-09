import math
a = int ( input (' nhập số a: '))
b = int ( input (' nhập số b: '))
c = int ( input (' nhập số c: '))
def xet_nghiem(a, b, c):
    if a == 0:
        return 'sai rồi, nhập lại đi'
    else:
        delta = math.pow (b, 2) - 4*a*c
        if delta < 0:
            return 'phương trình vô nghiệm'
        elif delta == 0:
            return 'phương trình có nghiệm kép x1 = x2 = ',-b/(2*a)
        else:
            return 'phương trình có hai nghiệm x1 = ', (-b-math.sqrt(delta)) / (2*a), ' và x2 = ', (-b+math.sqrt(delta)) / (2*a)
print ('kết quả: ', xet_nghiem(a, b, c))