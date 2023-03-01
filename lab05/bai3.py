
def chuyendoi(n):
    j = []
    while (n>0):
        a = int(float(n%2)) 
        j.append(a) 
        n = (n-a)/2 
    a1 = ""
    j.reverse() 
    for i in j:
        a1 += str(i)
    return a1
n = int(input("Nhap vao so thap phan: "))
print("So", n," co dang nhi phan la:", chuyendoi(n))