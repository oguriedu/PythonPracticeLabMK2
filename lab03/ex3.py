#3
import math
n=int(input("nhập giá trị n: "))
if n<0:
    print("nhập số tự nhiên: ")
elif n<2:
    print("{} không là số nguyên tố ",format(n))
else:
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0:
            print("{} không là số nguyên tố".format(n))
            break
    else:
        print("{} là số nguyên tố".format(n))