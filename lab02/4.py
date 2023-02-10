n=int(input("Nhập vào 1 số nguyên: "))
def tram(n):
    if n <= 99:
        print("0")
    else:
        m=str(n)
        print(m[-3])
tram(n) 