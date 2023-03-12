import random


lst=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print(lst)
#1
print('Phần tử thứ 2, thuộc vị trí thứ 3 là:',lst[2][1])
#2
print('Chiều dài của list:',len(lst))
lst_moi=[random.choice(["tomorrow"]),random.randint(1,200)]
lst.append(lst_moi)
print('List mới:',lst)
#3
s=0
for thu,giam_gia in lst:
    if thu=="mon" or thu=="tue" or thu=="sat" or thu=="sun":
        s+=giam_gia
print(s)