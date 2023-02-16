n = int(input('Nhập giá trị n :'))
print('Các số hoàn hảo nhỏ hơn',n,"là:")
def ktra_shh(n):
   tongCacUoc = 0
   for i in range(1, n // 2 + 1):
       if n % i == 0:
           tongCacUoc += i
   if n == tongCacUoc:
       return True
   return False
def lke_shh(n):
   for i in range(1, n):
       if ktra_shh(i):
           print(i, end=' ')
lke_shh(n)