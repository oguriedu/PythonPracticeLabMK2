#hệ cơ số 10 là hệ thập phân
n=int(input("Nhập số tự nhiên n: "))
i=[]
while n>0:
    i.append(str(n%2))
    n//=2
i.reverse()
i="".join(i)
print("Chuỗi nhị phân là:",i)