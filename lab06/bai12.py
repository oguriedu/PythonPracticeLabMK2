import os
clear='cls'
tk='Trần Mạnh Hùng'
stk='4891001032004'
money=0
history=[]

while True:
    print(f"""                                              
    -------------------NGÂN HÀNG xXxBANK-------------------------                      
      Tên tài khoản: {tk}                                         
      Số tài khoản: {stk}                                     
      Số dư tài khoản: {money}
    [1] Rút tiền 
    [2] Nạp tiền 
    [3] Kiểm tra lịch sử giao dịch                                    
    [0] Thoát                                                     
    """)
    chon=input()
    if chon=='1':
        Withdraw=int(input('W '))
        money-=Withdraw
        mess = f"Rút: {Withdraw} Số dư: {money}"
        history.append(mess)
        os.system(clear)
    elif chon=='2':
        Deposit=int(input('D '))
        money+=Deposit
        mess = f"Nạp: {Deposit} Số dư: {money}"
        history.append(mess)
        os.system(clear)
    elif chon=='3':
        os.system(clear)
        for i in history:
            print(i)
        input('Nhấn bất kỳ để tiếp tục')
        os.system(clear)
    elif chon=='4':
        print(history)
    elif chon=='0':
        break