def kiemtraHoanHao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False


n = int(input('Nhap vao so nguyen n lon hon 0: '))
if kiemtraHoanHao(n):
    print(n, ' la so hoan hao')
else:
    print(n, ' khong la so hoan hao')
    def liet_ke_so_hoan_thien(n):
       for i in range(1, n):
        if kiemtraHoanHao(i):
           print('những số hoàn hảo nhỏ hơn n là :',i)
try:
    n = int(input('nhập số nguyên :')) 
    if n < 0:
       print("Vui long nhap so tu nhien!")
    else:
       liet_ke_so_hoan_thien(n)
except:
   print("Dinh dang dau vao khong hop le!")