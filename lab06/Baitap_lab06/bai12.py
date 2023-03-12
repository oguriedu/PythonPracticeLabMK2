so_du=0
giao_dich=input('Nhập giao dịch:')
giao_dich_moi=giao_dich.split()
for i in range(len(giao_dich_moi)):
    if giao_dich_moi[i]=='D':
        so_du+=int(giao_dich_moi[i+1])
    elif giao_dich_moi[i]=='W':
        so_du-=int(giao_dich_moi[i+1])
print('Số dư thực tế:',so_du) 

