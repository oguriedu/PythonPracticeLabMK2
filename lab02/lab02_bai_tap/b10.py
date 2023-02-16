start_time = int(input("Nhập giờ bắt đầu (5-22): "))
end_time = int(input("Nhập giờ kết thúc (5-22): "))
time = end_time - start_time
if time <= 0:
    print("Nhập sai giờ.")
else:
    price = 0
    if start_time >= 5 and end_time <= 22:
        if time > 3:
            price = price + 3 * 100000
            time = time - 3
            hour_price = 100000 * 0.75
            price += time * hour_price
        else:
            price = time * 100000
        if 11 <= start_time and end_time <= 15:
            price = price - price * 0.1
        print(f"Tiền phải trả: {price}")
    else:
        print("Nhập sai giờ.")
