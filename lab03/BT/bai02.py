def kiem_tra_so_hoan_hao(n):
   tongCacUoc = 0
   for i in range(1, n // 2 + 1):
       if n % i == 0:
           tongCacUoc += i
   if n == tongCacUoc:
       return True
   return False
def liet_ke_so_hoan_hao(n):
   for i in range(1, n):
       if kiem_tra_so_hoan_hao(i):
           print(i, end=' ')
try:
   n = int(input("nhap vao so hoan hao : "))
   if n < 0:
       print("Vui long nhap so tu nhien!")
   else:
       liet_ke_so_hoan_hao(n)
except:
   print("khong hop le!")
