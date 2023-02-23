
bang = {0:'Không',1:'Một',2:'Hai',3:'Ba',4:'Bốn',5:'Năm',6:'Sáu',7:'Bảy',8:'Tám',9:'Chín'}
n=[int(i) for i in input('Nhập số từ bàn phím: ')]
m=0
while len(n)!=m:
    print(bang[n[m]],end=' ')
    m+=1