balance = 0

while True:
    inp = input("Nhập vào nhật ký giao dịch (D hoặc W số_tiền, nhập Q để thoát): ")
    if inp == "Q":
        break
    else:
        try:
            transaction_type, amount = inp.split()
            amount = int(amount)
            if transaction_type == "D":
                balance += amount
            elif transaction_type == "W":
                balance -= amount
        except:
            print("Lỗi: Vui lòng nhập đúng định dạng (D hoặc W số_tiền)")

print("Số tiền thực trong tài khoản: ", balance)
