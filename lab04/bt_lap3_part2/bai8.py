s=0
s2=0
n=int(input('Nhập giá trị n:'))
if n < 0:
    print('Không thỏa mãn yc đầu bài, mời bạn nhập lại!')
else:
        for i in range(1,n+1):
            s+=i
        print('Giá trị của dãy là:',s)

        for i in range(1,n+1,2):
                s+=(2*i+1)
        print('Giá trị của dãy là:',s)
        
        for i in range(2,n,2):
                    s+= 2*n
        print('Giá trị của dãy là:',s)