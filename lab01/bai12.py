import math
a=float(input('nhập vào a: '))
s=-math.pow(a,4)/math.log(4,5)+math.pow(a,4)*math.log(4,5)
if a>0:
    print('quãng đường là: ',abs(round(s,2)))
elif a<0:
    print("quãng đường là: ",round(s,2))