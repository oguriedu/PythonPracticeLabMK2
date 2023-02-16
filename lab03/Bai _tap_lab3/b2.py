def kiemtra_shh(n):
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum+=i
    if sum == n:
        return True
    else:
        return False
n=int(input("nhập vào số nguyên: "))
if kiemtra_shh(n):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")