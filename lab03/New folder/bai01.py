n=int(input("nhập n: "))
t=0
h=1
for i in range(n):
    m=(2*(i+1))/(2*i+3)
    h=h*m
    print(m,h)
    t+=h
print(t+1)