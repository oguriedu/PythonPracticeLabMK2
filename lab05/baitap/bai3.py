j= []
def ham(n):

    while (n>0):
        a = int(float(n%2))
        j.append(a) 
        n = (n-a)/2 
    kq = ""
    j.reverse()
    for i in j:
        kq += str(i)
    return kq
n = int(input("Nhap vao so thap phan: "))
print("Dạng nhị phân của số ",n,"là : ", ham(n))
