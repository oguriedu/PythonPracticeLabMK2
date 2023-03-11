n=int(input("Nhập n: "))
s=0
s1=0
while n>0:
    s=s+n%10
    n=int(n/10)
    s.reverse()
    print(int(s))
    s=0