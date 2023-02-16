'''
thực hiện phép toán
'''
n=int(input("nhập giá trị n: "))
t=1
s=1
for i in range(0,n+1):
    a=(2*(n+1))/((2*n)+3)
    s*=a
    t+=s
print("tổng là: ",t)