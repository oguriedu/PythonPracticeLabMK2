c = {0:'Không',1:'Một',2:'Hai',3:'Ba',4:'Bốn',5:'Năm',6:'Sáu',7:'Bảy',8:'Tám',9:'Chín'}
number=[int(i) for i in input('Nhập số từ bàn phím: ')]
tổng=0
while len(number)!=tổng:
    print(c[number[tổng]],end=' ')
    tổng+=1