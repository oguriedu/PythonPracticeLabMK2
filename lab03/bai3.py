n = int(input("hãy nhập số n : "))
if n == 2 or n == 3 or n == 5 or n == 7:
    print("n la so nguyen to")
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print("n là số nguyên tố")
else:
    print("n không phải là số nguyên tố ")