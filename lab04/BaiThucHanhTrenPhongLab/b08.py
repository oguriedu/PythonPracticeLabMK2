while True:
    n = input("Nhap ky tu: ")
    if len(n) > 1:
        continue
    elif len(n) == 0:
        break
    else:
        print(f"Gia tri ascii: {ord(n)}")
