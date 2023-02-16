n = int(input('Nhập giá trị n :'))
def ktra_snt(n):
    flag = True
    if n<2:
        flag = False
    else:
        for i in range (2,n):
            if n%i==0:
                flag = False
    return flag

