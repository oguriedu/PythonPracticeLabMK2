#chương trình nhập số bất kì
n=int(input("nhập số n = "))
while n<=0:
    print("hãy nhập lại cho chính xác ")
    n=int(input("nhập số n = "))
print('số đã nhập là :',n)