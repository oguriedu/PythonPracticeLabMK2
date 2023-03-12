import random


so=[i for i in range(210) if i%5==0 and i%7==0]
if len(so)>0:
        so_ngau_nhien=random.choice(so)
        print(so_ngau_nhien)
else:
        print('Không có số nào thỏa mãn yêu cầu')
