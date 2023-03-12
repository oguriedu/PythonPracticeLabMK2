import os
clear = 'cls'
tk = 'Vũ Như An'
stk = '0326001421'
money = 0
history = []

while True:
    print(f"""                                              
    -------------------NGÂN HÀNG TP BANK-------------------------                      
      Tên chủ tài khoản: {tk}                                         
      Số tài khoản: {stk}                                     
      Số dư tài khoản: {money}
    [1] Rút tiền 
    [2] Nạp tiền 
    [3] Kiểm tra lịch sử giao dịch                                    
    [0] Thoát                                                     
    """)
    chon = input()
    if chon=='1':
        Withdraw = int(input('W '))
        money-=Withdraw
        mess = f"Rút: {Withdraw} Số dư: {money}"
        history.append(mess)
        os.system(clear)
    elif chon=='2':
        Deposit = int(input('D '))
        money+=Deposit
        mess = f"Nạp: {Deposit} Số dư: {money}"
        history.append(mess)
        os.system(clear)
    elif chon=='3':
        os.system(clear)
        for i in history:
            print(i)
        input('Nhấn phím Enter để tiếp tục')
        os.system(clear)
    elif chon=='0':
        break
