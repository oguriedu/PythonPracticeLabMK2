kw = int(input("Nhập số KW tiêu thụ: "))
if kw <= 100:
    price = 2000
elif kw <= 200:
    price = 2500
elif kw <= 300:
    price = 3000
else:
    price = 5000
print(f"Tổng tiền điện là: {kw*price} đồng")
