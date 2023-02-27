bang = {0:'khong',1:'mot',2:'hai',3:'Ba',4:'bon',5:'nam',6:'sau',7:'bay',8:'tam',9:'chin'}
n=[int(i) for i in input('Nhập số từ bàn phím: ')]
m=0
while len(n)!=m:
    print(bang[n[m]])
    m+=1