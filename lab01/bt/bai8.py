lstCuaHang=[]
def them_cua_hang(lstCuaHang):
    while True:
        ma_ch=input("Nhập mã cửa hàng:")
        ten_ch=input("Nhập tên cửa hàng:")
        von_dau_tu=float(input(" Nhập vốn đầu tư:"))
        doanh_thu=float(input("Nhập doanh thu:")) 
        tt=input(" bạn có muốn tiếp tục không? (1:TT)")
        lstCuaHang.append({'ma_ch':ma_ch,'ten_ch':ten_ch,'von_dau_tu':von_dau_tu,'doanh_thu': doanh_thu})
        if tt!='1':
            print("helo")
            break 
           
    return 
them_cua_hang(lstCuaHang)