n=int(input('Nhập n:'))

for i in range(1,n):
      a=0
      for j in range(1,i):
            if (i%j) == 0:
                  a+=j
      if a == i:
                  print('các số hoàn hảo nhỏ thua n là:',i)
