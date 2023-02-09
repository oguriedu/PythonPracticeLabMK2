so_can_tim_hang_tram=int(input("hãy nhập số : "))
if so_can_tim_hang_tram >=100:
    print("hàng trăm trong số ",so_can_tim_hang_tram,"là ",(so_can_tim_hang_tram // 100)%10)
else:
    print("0")