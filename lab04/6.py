number= {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
n=[int(i) for i in input('Nhập số từ bàn phím: ')]
m=0
while len(n)!=m:
    print(number[n[m]],end=' ')
    m+=1