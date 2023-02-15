def kiemtra(n):
    tong=0
    for i in range(1,n):
        if (n%i==0):
            tong=tong+i
    if tong == n:
        return True
    else:
        return False
n=int(input("nhập vào số nguyên: "))
if kiemtra(n):
    print(n,"là số hoàn hảo")
else:
    print("không là số hoàn hảo")