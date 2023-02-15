#chương trình in ra số nguyên tố bé hơn hoặc bằng n
n = int(input("Nhập số n = : "))
print("Các sô nguyên tố nhỏ hơn hoặc bằng ", n, "là:")
for i in range(2, n+1):
    x= True
    for j in range(2,int(i**(1/2)+1)):
        if i % j == 0:
            x= False
            break
    if x:
        print(i)