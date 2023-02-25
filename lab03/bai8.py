n = int(input("Nhập n: "))
if n <= 0:
    n = int(input("Nhập lại n (n > 0): "))
S1=0
S2=0
S3=0
S1 = (n*(n + 1))/2
S2 = (n + 1)**2
S3 = n*(n + 1)
print("tong s1 la: ", S1)
print("tong s2 la:  ", S2)
print("tong s3 la: ", S3)