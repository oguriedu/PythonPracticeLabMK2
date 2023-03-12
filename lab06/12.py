balance = 0  # Số dư ban đầu là 0

while True:
    transaction = input('Nhập giao dịch (D hoặc W và số tiền, hoặc Enter để hoàn tất): ')
    if not transaction:  # Nếu không nhập giao dịch nữa thì dừng vòng lặp
        break
    
    transaction_type, amount = transaction.split()
    amount = int(amount)
    
    if transaction_type == 'D':
        balance += amount
    elif transaction_type == 'W':
        balance -= amount
    
print('Số tiền thực trong tài khoản là:', balance)
