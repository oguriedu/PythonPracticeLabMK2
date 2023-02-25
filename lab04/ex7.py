a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
def uoc(a,b):
    while b:
        a, b = b,a%b
        return a
def boichung(a,b):
    return a*b // uoc(a,b)
boichung_min=boichung(a,b)
print("Bội chung nhỏ nhất là:",boichung_min)
