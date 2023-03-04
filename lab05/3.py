n = int(input(" nhập một số tự nhiên từ bàn phím :"))
hnp= ""
while n>0:
    hnp = str(n%2) + hnp
    n=  n//2
print (" hệ nhị phân :", hnp)

