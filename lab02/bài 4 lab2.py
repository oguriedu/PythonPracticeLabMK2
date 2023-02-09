def hundreds_digit(num):
    if abs(num) >= 100:
        return num // 100 % 10
    return 0

num = int(input("Enter an integer: "))
print("Hundreds digit:", hundreds_digit(num))
