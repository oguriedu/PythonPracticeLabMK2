m = input("Nhap van ban:")
n = input("Nhap tu can tim:")
try:
    print(f"{n} xuat hien {m.count(n)} lan trong van ban")
except:
    print(f"{n} khong co trong {m}")