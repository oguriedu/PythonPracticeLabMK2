n = int(input("Nhập vào một số nguyên: "))
ktNT = True
i = 2
while i*i <= n:
    if (n % i == 0):
        ktNT = False
        break
    i += 1

if (ktNT and n != 1):
    print(n, " là số nguyên tố!")
else:
    print(n, " không phải là số nguyên tố!!")
