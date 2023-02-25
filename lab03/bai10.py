#phân tích thừa sô nguyên tố
n = int(input("Nhập n số nguyên dương: "))
print("Phân tích thừa số nguyên tố của", n, "=")
i = 2
while i <= n:
    dem = 0
    while n % i == 0:
        n //= i
        dem += 1
    if dem> 0:
        print(i,"x",dem, end="" ) 
    i += 1