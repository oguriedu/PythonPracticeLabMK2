n=int(input("Enter interger:"))
def a(n):
    if n==1:
        return 1
    else:
        return ((1/n)+a(n-1))
print(a(n))